#!/usr/bin/python3
"""
Markdown to HTML Converter
convert heading
"""

from os.path import isfile
import sys

def file_exist(argv):
    """Verify if the necessary files exist and if the correct number of arguments are provided."""
    if len(argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    if not isfile(argv[1]):
        print("Missing " + argv[1], file=sys.stderr)
        sys.exit(1)

def markdown_to_html(md_file, html_file):
    """Converts a Markdown file to HTML."""
    try:
        with open(md_file, 'r') as f:
            lines = f.readlines()  # Corrigé pour lire toutes les lignes

        with open(html_file, 'w') as f:
            in_list = False  # Initialisation de in_list

            for index in lines:
                index = index.strip()

                if index.startswith('#'):
                    level = index.count('#')
                    heading = index.strip('#').strip()
                    html_heading = f'<h{level}>{heading}</h{level}>'
                    f.write(html_heading + '\n')

                elif index.startswith('-'):
                    if not in_list:
                        f.write('<ul>\n')
                        in_list = True
                    list_item = index.strip('-').strip()
                    f.write(f'<li>{list_item}</li>\n') # Create a list item

                else:
                    if in_list:
                        f.write('</ul>\n')
                        in_list = False

            # Close the <ul> tag if the list has not been closed.
            if in_list:
                f.write('</ul>\n')

    except IOError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    file_exist(sys.argv)
    markdown_to_html(sys.argv[1], sys.argv[2])
