# This file will house the functionality for remote deployment over PubKey based SSH.
import subprocess
import click

def run_remote_command(command):
    """Run command on remote machine"""
    
    return

@click.command()
@click.option('--host', '-h', required=True)
@click.option('--dir', '-d', default="./")
@click.option('--theme-only', '-t')
@click.option('--db-only', '-db')
@click.option('--backup', '-b', help="Backup destination DB & files before deployment")
def deploy(host, dir, theme_only, db_only, backup):
    """Sync files to remote machine"""

    return
