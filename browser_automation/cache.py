import click
import subprocess

@click.group()
def cache():
    """WordPress Only: Flush the cache"""
    pass

@click.command()
@click.option('--cache-only', '-c', default=False)
def flush(cache_only):
    """WordPress Only: Flush cache and rewrites"""
    try:
        subprocess.run(["wp --exec='error_reporting(E_ALL ^ E_DEPRECATED);'", "cache", "flush"])
        if not cache_only:
            subprocess.run(["wp --exec='error_reporting(E_ALL ^ E_DEPRECATED);'", "rewrite", "clear"])
    except:
        click.echo(click.style('Could not dump database', fg='red', bold=True))
        click.confirm('Do you want to continue?', abort=True)
    return

cache.add_command(flush)
