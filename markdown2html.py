#!/usr/bin/env python3
"""This module takes a readme text and translates it to html code"""
import sys
import os


def convert_markdown_to_html(markdown_file, output_file):
    """ The function responiable of transforming from markdown to html code"""
    with open(markdown_file, 'r') as md_file, open(output_file,
                                                   'w') as html_file:
        for line in md_file:
            line = line.rstrip()
            if line.startswith('#'):
                header_level = line.count('#', 0, 6)
                if header_level > 0 and line[header_level] == ' ':
                    content = line[header_level + 1:]
                    html_file.
                    write(f'<h{header_level}>{content}</h{header_level}>\n')
            else:
                html_file.write(line + '\n')


def main():
    """main function that checks for argument length"""
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    convert_markdown_to_html(markdown_file, output_file)

    sys.exit(0)


if __name__ == "__main__":
    main()
