#!/usr/bin/python3
"""This module takes a readme text and translates it to html code"""
import sys
import os


def convert_markdown_to_html(markdown_file, output_file):
    """ The function responsiable of transforming from markdown to html code"""
    with open(markdown_file, 'r') as md_file, open(output_file,
                                                   'w') as html_file:
        in_ulist = False
        in_olist = False
        in_paragraph = False

        for line in md_file:
            line = line.rstrip()

            # Convert bold syntax using ** and __
            line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
            line = re.sub(r'__(.*?)__', r'<b>\1</b>', line)

            # Heading parsing
            if line.startswith('#'):
                if in_ulist:
                    html_file.write('</ul>\n')
                    in_ulist = False
                if in_olist:
                    html_file.write('</ol>\n')
                    in_olist = False
                if in_paragraph:
                    html_file.write('</p>\n')
                    in_paragraph = False

                header_level = line.count('#', 0, 6)
                if header_level > 0 and line[header_level] == ' ':
                    content = line[header_level + 1:]
                    html_file.write
                    (f'<h{header_level}>{content}</h{header_level}>\n')

            # Unordered list parsing
            elif line.startswith('- '):
                if in_olist:
                    html_file.write('</ol>\n')
                    in_olist = False
                if in_paragraph:
                    html_file.write('</p>\n')
                    in_paragraph = False
                if not in_ulist:
                    html_file.write('<ul>\n')
                    in_ulist = True
                content = line[2:]
                html_file.write(f'<li>{content}</li>\n')

            # Ordered list parsing
            elif line[0].isdigit() and line[1] == '.' and line[2] == ' ':
                if in_ulist:
                    html_file.write('</ul>\n')
                    in_ulist = False
                if in_paragraph:
                    html_file.write('</p>\n')
                    in_paragraph = False
                if not in_olist:
                    html_file.write('<ol>\n')
                    in_olist = True
                content = line[3:]
                html_file.write(f'<li>{content}</li>\n')

            # Paragraph parsing
            elif line.strip():
                if in_ulist:
                    html_file.write('</ul>\n')
                    in_ulist = False
                if in_olist:
                    html_file.write('</ol>\n')
                    in_olist = False
                if not in_paragraph:
                    html_file.write('<p>\n')
                    in_paragraph = True
                html_file.write(line + '\n')

            # Empty line handling
            else:
                if in_paragraph:
                    html_file.write('</p>\n')
                    in_paragraph = False
                html_file.write(line + '\n')

        if in_ulist:
            html_file.write('</ul>\n')
        if in_olist:
            html_file.write('</ol>\n')
        if in_paragraph:
            html_file.write('</p>\n')


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
