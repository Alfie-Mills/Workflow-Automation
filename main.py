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

@cli.command()
@click.option('-n', '--name', type=str, help='Name to greet', default='World')
def hello(name):
    click.echo(f'Hello {name}')

# TODO: Write the main function to do the things