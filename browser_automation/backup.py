# Parts of this code was origially a bash script, converted into Python3 by OpenAI's ChatGPT

# Importing the necessary modules
import datetime
import os
import random
import subprocess
import click
from browser_automation.helpers import command

@click.command()
@click.option('--dir', '-d', required=True, default="~/public_html")
@click.option('--site-content', '-c', default="wp-content")
def backup(dir, site_content):
    
    if not os.path.exists(os.path.abspath(site_content)):
        click.echo(f"{site_content} does not exist")
        return
    
    if not os.path.exists(os.path.abspath(dir)):
        click.echo(f"{dir} does not exist")
        return

    if not command("wp"):
        click.echo("WP command not available")
        return

    click.echo(f" Making Backup of {os.path.abspath(dir)}")
    # Setting the directory to the public_html folder
    os.chdir(os.path.abspath(dir))

    # # # Creating the backups directory if it doesn't exist
    if not os.path.exists(os.path.expanduser("~/wfa-backups")):
        click.echo("Creating backups directory: {os.path.abspath}")
        os.makedirs(os.path.expanduser("~/wfa-backups"))

    # # # Generating a random ID
    # id = random.randint(0, 999999)

    # if which(wp) is not None:
    
    # # # Dumping the database
    # subprocess.run(["wp", "db", "dump", os.path.expanduser("~/backups/") + 
    #     f"{datetime.date.today():%d%m%y}" + f"{id}_db.sql"])

    # # Zipping the wp-content folder
    # subprocess.run(["zip", "-r", os.path.expanduser("~/backups/") + 
    #     f"{datetime.date.today():%d%m%y}" + f"{id}_wp-content.zip", 
    #     "./wp-content/plugins/", "./wp-content/mu-plugins/", "./wp-content/themes/"])

    # # Changing the directory back to the previous one
    # os.chdir("-")

    # # Printing the success message
    # print("\033[1;32mBackup #{datetime.date.today():%d%m%y}{id} Complete\033[0m")

def test():
    print("it worked")