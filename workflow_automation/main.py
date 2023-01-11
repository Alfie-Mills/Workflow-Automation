# Importing the necessary modules
import click
from workflow_automation.backup import *
from workflow_automation.cache import cache

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    """
    Command line tool to manage websites

    Some command are specific to wordpress, such as she cache module.
    """
    pass

cli.add_command(backup)

cli.add_command(cache)

if __name__ == '__main__':
    cli()