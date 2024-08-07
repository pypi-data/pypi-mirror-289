import os
import sys
import time
from typing import Dict, List, Optional, Union

import typer
import json
from rich.console import Console
from rich.syntax import Syntax

from guardrails.cli.guardrails import guardrails as gr_cli
from guardrails.cli.hub.install import (  # JC: I don't like this import. Move fns?
    install_hub_module,
    add_to_hub_inits,
    run_post_install,
)
from guardrails.cli.hub.utils import get_site_packages_location
from guardrails.cli.server.hub_client import get_validator_manifest
from guardrails.cli.hub.template import get_template

console = Console()


@gr_cli.command(name="create")
def create_command(
    validators: Optional[str] = typer.Option(
        default="",
        help="A comma-separated list of validator hub URIs.",
    ),
    name: Optional[str] = typer.Option(
        default=None, help="The name of the guard to define in the file."
    ),
    filepath: str = typer.Option(
        default="config.py",
        help="The path to which the configuration file should be saved.",
    ),
    template: Optional[str] = typer.Option(
        default=None,
        help="Then hub uri to template to base the configuration file on."
        " For example hub:template://guardrails/chatbot or hub:template://guardrails/summarizer."
        " Files paths ending in .json are also accepted."
        " If this option is set, validators should not be provided.",
    ),
    dry_run: bool = typer.Option(
        default=False,
        is_flag=True,
        help="Print out the validators to be installed without making any changes.",
    ),
):
    filepath = check_filename(filepath)

    if not validators and template is not None:
        template_dict, template_file_name = get_template(template)
        validators_map: Dict[str, bool] = {}
        for guard in template_dict["guards"]:
            for validator in guard["validators"]:
                validators_map[f"hub://{validator['id']}"] = True
        validators = ",".join(validators_map.keys())
        installed_validators = split_and_install_validators(validators, dry_run)  # type: ignore
        new_config_file = generate_template_config(
            template_dict, installed_validators, template_file_name
        )
    elif not validators and template is None:
        console.print(
            "No validators or template provided. Please run `guardrails create --help`"
            " for options and details."
        )
        sys.exit(1)
    else:
        installed_validators = split_and_install_validators(validators, dry_run)  # type: ignore
        if name is None and validators:
            name = "Guard"
            if len(installed_validators) > 0:
                name = installed_validators[0] + "Guard"

            console.print(f"No name provided for guard. Defaulting to {name}")
        new_config_file = generate_config_file(installed_validators, name)

    if dry_run:
        console.print(f"Not actually saving output to [bold]{filepath}[/bold]")
        console.print("The following would have been written:\n")
        formatted = Syntax(new_config_file, "python")
        console.print(formatted)
        console.print("\n")
    else:
        with open(filepath, "wt") as fout:
            fout.write(new_config_file)
        console.print(f"Saved configuration to {filepath}")
    console.print(
        f"Replace TODOs in {filepath} and run with `guardrails start"
        f" --config {filepath}`"
    )


def generate_template_config(
    template: dict, installed_validators, template_file_name
) -> str:
    # Read the template file
    script_dir = os.path.dirname(os.path.realpath(__file__))
    config_template_path = os.path.join(
        script_dir, "hub", "template_config.py.template"
    )

    with open(config_template_path, "r") as file:
        template_content = file.read()
    guard_instantiations = []

    for i, guard in enumerate(template["guards"]):
        guard_instantiations.append(f"guard{i} = Guard.from_dict(guards[{i}])")
    guard_instantiations = "\n".join(guard_instantiations)
    # Interpolate variables
    output_content = template_content.format(
        TEMPLATE_FILE_NAME=template_file_name,
        GUARDS=json.dumps(template["guards"], indent=4),
        VALIDATOR_IMPORTS=", ".join(installed_validators),
        GUARD_INSTANTIATIONS=guard_instantiations,
    )

    return output_content


def check_filename(filename: Union[str, os.PathLike]) -> str:
    """If a filename is specified and already exists, will prompt the user to
    confirm overwriting.

    Aborts if the user declines.
    """
    if os.path.exists(filename):
        # Alert the user and get confirmation of overwrite.
        overwrite = typer.confirm(
            f"The configuration file {filename} already exists. Overwrite?"
        )
        if not overwrite:
            console.print("Aborting")
            typer.Abort()
            sys.exit(0)  # Force exit if we fall through.
    return filename  # type: ignore


def split_and_install_validators(validators: str, dry_run: bool = False):
    """Given a comma-separated list of validators, check the hub to make sure
    all of them exist, install them, and return a list of 'imports'.

    If validators is empty, returns an empty list.
    """
    if not validators:
        return []

    stripped_validators = list()
    manifests = list()
    site_packages = get_site_packages_location()

    # Split by comma, strip start and end spaces, then make sure there's a hub prefix.
    # If all that passes, download the manifest file so we know where to install.
    # hub://blah -> blah, then download the manifest.
    console.print("Checking validators...")
    with console.status("Checking validator manifests") as status:
        for v in validators.split(","):
            v = v.strip()
            status.update(f"Prefetching {v}")
            if not v.startswith("hub://"):
                console.print(
                    f"WARNING: Validator {v} does not appear to be a valid URI."
                )
                sys.exit(-1)
            stripped_validator = v.lstrip("hub://")
            stripped_validators.append(stripped_validator)
            manifests.append(get_validator_manifest(stripped_validator))
    console.print("Success!")

    # We should make sure they exist.
    console.print("Installing...")
    with console.status("Installing validators") as status:
        for manifest, validator in zip(manifests, stripped_validators):
            status.update(f"Installing {validator}")
            if not dry_run:
                install_hub_module(manifest, site_packages, quiet=True)
                run_post_install(manifest, site_packages)
                add_to_hub_inits(manifest, site_packages)
            else:
                console.print(f"Fake installing {validator}")
                time.sleep(1)
    console.print("Success!")

    # Pull the hub information from each of the installed validators and return it.
    return [manifest.exports[0] for manifest in manifests]


def generate_config_file(validators: List[str], name: Optional[str] = None) -> str:
    console.print("Generating config file...")
    config_lines = [
        "from guardrails import Guard",
    ]

    # Import one or more validators.
    if len(validators) == 1:
        config_lines.append(f"from guardrails.hub import {validators[0]}")
    elif len(validators) > 1:
        multiline_import = ",\n\t".join(validators)
        config_lines.append(f"from guardrails.hub import (\n\t{multiline_import}\n)")

    # Initialize our guard.
    config_lines.append("guard = Guard()")
    if name is not None:
        config_lines.append(f"guard.name = {name.__repr__()}")

    # Warn the user that they need to update their config file.
    config_lines.append(
        'print("GUARD PARAMETERS UNFILLED! UPDATE THIS FILE!")'
        "  # TODO: Remove this when parameters are filled."
    )

    # Append validators:
    if len(validators) == 1:
        config_lines.append(f"guard.use({validators[0]}())  # TODO: Add parameters.")
    elif len(validators) > 1:
        multi_use = "".join(
            [
                "\t" + validator + "(),  # TODO: Add parameters.\n"
                for validator in validators
            ]
        )
        config_lines.append(f"guard.use_many(\n{multi_use})")

    return "\n".join(config_lines)
