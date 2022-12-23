# Parts of this code was origially a bash script, converted into Python3 by OpenAI's ChatGPT

# Importing the necessary modules
import datetime
import os
import random
import subprocess

def backup():
    # Setting the directory to the public_html folder
    os.chdir(os.path.expanduser("~/public_html"))

    # Creating the backups directory if it doesn't exist
    if not os.path.exists(os.path.expanduser("~/backups")):
        os.makedirs(os.path.expanduser("~/backups"))

    # Generating a random ID
    id = random.randint(0, 999999)

    # Dumping the database
    subprocess.run(["wp", "db", "dump", os.path.expanduser("~/backups/") + 
        f"{datetime.date.today():%d%m%y}" + f"{id}_db.sql"])

    # Zipping the wp-content folder
    subprocess.run(["zip", "-r", os.path.expanduser("~/backups/") + 
        f"{datetime.date.today():%d%m%y}" + f"{id}_wp-content.zip", 
        "./wp-content/plugins/", "./wp-content/mu-plugins/", "./wp-content/themes/"])

    # Changing the directory back to the previous one
    os.chdir("-")

    # Printing the success message
    print("\033[1;32mBackup #{datetime.date.today():%d%m%y}{id} Complete\033[0m")

def test():
    print("it worked")