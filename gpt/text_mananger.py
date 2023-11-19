# pip3 install python-docx --user

import docx
import rakeai_gpt

def modify(file_name: str) -> None:
    doc = docx.Document(file_name)
    count  = 0
    for para in doc.paragraphs:
        chunk = para.text
        size = len(chunk)
        print("new paragraphs: " + str(size))
        if(size > 1900):
            print("warning: this is too long")
        new_chunk = rakeai_gpt.fixGrammer(chunk)
        print(new_chunk)
        para.text = new_chunk
        count += 1;
        if count >= 10:
            break
        doc.save("sample.docx")

modify("sample.docx")
