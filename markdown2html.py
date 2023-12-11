#!/usr/bin/python3
"""Script that converts Markdown to HTML."""

from os.path import isfile
import sys
import markdown


def file_exist(argv):
    """Verify if the necessary files exist and if the correct number of arguments are provided.
    
    Args:
        argv (list of str): Command line arguments where argv[1] is the source Markdown file
                            and argv[2] is the destination HTML file.
    """
    if len(argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    if isfile(argv[1]) is False:
        print("Missing " + argv[1], file=sys.stderr)
        sys.exit(1)

    sys.exit(0)


def markdown_html(argv):
    """Convert the content of a Markdown file to HTML and save it to a specified file.
    
    Args: argv (list of str): Command line arguments where argv[1] is the source Markdown file
                            and argv[2] is the destination HTML file.
    """
    with open(argv[1], 'r') as file:
        markdown_string = file.read()

    html_string = markdown.markdown(markdown_string)

    with open(argv[2], 'w') as new_file:
        new_file.write(html_string)


if __name__ == "__main__":
    file_exist(sys.argv)
    markdown_html(sys.argv)
