import win32com.client as win32
import os
import re
from datetime import datetime

word = win32.Dispatch("Word.Application")
word.Visible = 0
word.Documents.Open(os.getcwd() + "/Invoicebox_v3.docx")
document = word.ActiveDocument
sections = document.Sections

paragraphs = document.Paragraphs
print( 'Number of paragraphs: ', paragraphs.count)

document.Paragraphs.Add()
title = document.Paragraphs(1) 
title.Range.Text = '«Инвойсбокс» API v3\n'

for section in sections:
    headersCollection = section.Headers
    for header in headersCollection:
        header.Range.Text = header.Range.Text + "«Инвойсбокс» API v3 (актуально на " + datetime.today().strftime('%d.%m.%Y') + ")"
        print(header.Range.Text)

#    for paragraph in section.Range.Paragraphs:
#        Text = paragraph.Range.Text
#        Text = re.sub("Читать далее »", "", Text)
#        paragraph.Range.Text = Text
