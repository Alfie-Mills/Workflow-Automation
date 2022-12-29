import click
import subprocess
from browser_automation.helpers import command

@click.group()
def cache():
    """WordPress Only: Flush the cache"""
    pass

@click.command()
@click.option('--cache-only', '-c', default=False)
def flush(cache_only):
    """WordPress Only: Flush cache and rewrites"""

    if not command("wp"):
        click.style("WP command not available", fg='red', bold=True)
        return

    try:
        subprocess.run(["wp --exec='error_reporting(E_ALL ^ E_DEPRECATED);'", "cache", "flush"])
        if not cache_only:
            subprocess.run(["wp --exec='error_reporting(E_ALL ^ E_DEPRECATED);'", "rewrite", "clear"])
    except:
        click.echo(click.style('Could not flush cache', fg='red', bold=True))
    return

cache.add_command(flush)
