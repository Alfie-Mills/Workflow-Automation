# Importing the necessary modules
import argparse
import click
from workflow_automation.backup import *
from workflow_automation.cache import cache

# #  Parse arguments
# parser = argparse.ArgumentParser()
# parser.add_argument("-b", "--backup")
# parser.add_argument("-p", "--production")
# parser.add_argument("-s", "--staging")
# parser.add_argument("-d", "--development")
# args = parser.parse_args()
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