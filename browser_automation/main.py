# Importing the necessary modules
import argparse
import click
from browser_automation.backup import *

# #  Parse arguments
# parser = argparse.ArgumentParser()
# parser.add_argument("-b", "--backup")
# parser.add_argument("-p", "--production")
# parser.add_argument("-s", "--staging")
# parser.add_argument("-d", "--development")
# args = parser.parse_args()

@click.group()
def cli():
    pass

cli.add_command(backup)

if __name__ == '__main__':
    cli()