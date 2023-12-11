#!/usr/bin/python3
"""
Markdown to HTML Converter
Task 0: convert heading
"""

from os.path import isfile
import sys
import os


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


def markdown_to_html(md_file, html_file):
    """Defines a function to convert a Markdown file to HTML.

    md_file: path to the Markdown file to convert.
    html_file: path to the output HTML file.
    """
    with open(md_file, 'r') as f:
        lines = f.readlines(0)

    with open(html_file, 'w') as f:
        """
        Opens the HTML file for writing.
        Any existing content will be replaced.
        """

        for index in lines:
            index = index.strip()

            if index.startswith('#'):
                """
                If the line is a Markdown title
                (starts with '#'), convert.
                """
                level = index.count('#')
                heading = index.strip('#').strip()
                html_heading = f'<h{level}>{heading}</h{level}>'
                f.write(html_heading + '\n')


if __name__ == "__main__":
    file_exist(sys.argv)
    markdown_to_html(sys.argv[1], sys.argv[2])
