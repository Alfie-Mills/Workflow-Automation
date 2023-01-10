import click
import subprocess
from browser_automation.helpers import command
from browser_automation.helpers import wp_default_args

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
        subprocess.run(["wp", wp_default_args, "cache", "flush"])
        if not cache_only:
            subprocess.run(["wp", wp_default_args, "rewrite", "clear"])
    except:
        click.echo(click.style('Could not flush cache', fg='red', bold=True))
    return

cache.add_command(flush)
