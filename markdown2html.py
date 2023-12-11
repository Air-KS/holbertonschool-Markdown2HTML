#!/usr/bin/python3
"""Scritp that convert markdown to html"""

from os.path import isfile
import sys
import markdown


def fileExist(argv):
    """Verify if the necessary files exist and if the correct number of arguments are provided.
    
    Args: argv (list of str): Command line arguments where argv[1] is the source Markdown file
                         and argv[2] is the destination HTML file.
    """
    if len(argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)

    if isfile(argv[1]) is False:
        print("Missing " + argv[1], file=sys.stderr)
        exit(1)

    exit(0)

if __name__ == "__main__":
    fileExist(sys.argv)
