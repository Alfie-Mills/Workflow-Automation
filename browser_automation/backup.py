# Parts of this code was origially a bash script, converted into Python3 by OpenAI's ChatGPT

# Importing the necessary modules
import datetime
import os
import shutil
import zipfile
import random
import subprocess
import click
import time
from browser_automation.helpers import command

@click.command()
@click.option('--dir', '-d', required=True, default="~/public_html")
@click.option('--site-content', '-c', default="wp-content")
@click.option('--site-content-include', '-ci', default=["/plugins", "/themes"])
def backup(dir, site_content, site_content_include):

    # with click.progressbar(length=100, label="backing up") as bar:
    #     for i in range(100):
    #         bar.update(i)
    #         time.sleep(0.1)
    #
    # print("Backup complete")
    
    if not os.path.exists(os.path.abspath(site_content)):
        click.echo(f"{site_content} does not exist")
        return
    
    if not os.path.exists(os.path.abspath(dir)):
        click.style(f"{dir} does not exist", fg='red', bold=True)
        return

    if not command("wp"):
        click.style("WP command not available", fg='red', bold=True)
        return

    click.echo(f" Making Backup of {os.path.abspath(dir)}")
    # Setting the directory to the public_html folder
    os.chdir(os.path.abspath(dir))

    # # # Creating the backups directory if it doesn't exist
    if not os.path.exists(os.path.expanduser("~/wfa-backups")):
        click.echo("Creating backups directory: {os.path.abspath}")
        os.makedirs(os.path.expanduser("~/wfa-backups"))

    # # Generating a random ID
    id = random.randint(1, 999999)
    
    # # Dumping the database
    try:
        subprocess.run(["wp --exec='error_reporting(E_ALL ^ E_DEPRECATED);'", "db", "dump", os.path.expanduser("~/wfa-backups/") + 
            f"{datetime.date.today():%d%m%y}" + f"{id:06}_db.sql"])
    except:
        click.echo(click.style('Could not dump database', fg='red', bold=True))
        click.confirm('Do you want to continue?', abort=True)

    zip_name= "dev.zip"

    # TODO: fix this 🤦‍♀️
    site_content_include=["/plugins", "/themes"]

    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
        for path in site_content_include:
            for folder_name, subfolders, filenames in os.walk(site_content + path):
                for filename in filenames:
                    file_path = os.path.join(folder_name, filename)
                    zip_ref.write(file_path, arcname=os.path.relpath(file_path, site_content))

    zip_ref.close()


    # # Zipping the wp-content folder
    # subprocess.run(["zip", "-rq", os.path.expanduser("~/wfa-backups/") + 
    #     f"{datetime.date.today():%d%m%y}" + f"{id}_wp-content.zip", 
    #     "./wp-content/plugins/", "./wp-content/mu-plugins/", "./wp-content/themes/"])

    # Printing the success message
    click.echo(f"\033[1;32mBackup #{datetime.date.today():%d%m%y}{id} Complete\033[0m")

def test():
    print("it worked")