from typing import Optional
import click
from toot import api, config
from toot.entities import Data
from toot.output import print_diags
from toot.cli import cli


@cli.command()
@click.option(
    "-f",
    "--files",
    is_flag=True,
    help="Print contents of the config and settings files in diagnostic output",
)
@click.option(
    "-s",
    "--server",
    is_flag=True,
    help="Print information about the curren server in diagnostic output",
)
def diag(files: bool, server: bool):
    """Display useful information for diagnosing problems"""
    instance_dict: Optional[Data] = None
    if server:
        _, app = config.get_active_user_app()
        if app:
            instance_dict = api.get_instance(app.base_url).json()

    print_diags(instance_dict, files)
