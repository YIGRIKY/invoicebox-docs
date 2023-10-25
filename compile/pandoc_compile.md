---
nav_exclude: true
search_exclude: true
date: 2023-10-25 00:00:00 +0300
---

Usage: pancompile DIRECTORY FILENAME [filemask] ["options"]
Uses pandoc to compile all documents in specified directory and subdirectories to a single output document

DIRECTORY         the directory/folder to parse recursively (passed to pandoc -s);
                  use quotation marks if there are spaces in the directory name
FILENAME          the output file (passed to pandoc -o); use quotation marks if spaces
filemask          an optional file mask/filter, e.g. *.md; leave blank for all files
"options"         optional list of pandoc commands (must be in quotation marks)

Minimal example: pancompile docs complete_book.docx
Typical example: pancompile "My Documents" "Complete Book.docx" *.md "-f markdown -t docx --standalone --toc"