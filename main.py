# Importing the necessary modules
import argparse
from backup import *
#  Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("-b", "--backup")
parser.add_argument("-p", "--production")
parser.add_argument("-s", "--staging")
parser.add_argument("-d", "--development")
args = parser.parse_args()

# TODO: Write the main function to do the things