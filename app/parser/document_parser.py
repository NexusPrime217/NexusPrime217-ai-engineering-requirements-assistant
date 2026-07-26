import pymupdf
import docx
import io
from docx import Document


def extract_txt(contents : bytes) -> str:
    return contents.decode("utf-8")

def extract_pdf(contents : bytes) -> str:
    text=""
    with pymupdf.open(stream=contents,filetype="pdf") as doc:
        for page in doc:
            text += page.get_text() + "\n"
    return text

def extract_docx(contents : bytes) -> str:
    text = ""
    content_stream = io.BytesIO(contents)
    doc = Document(content_stream)
    for paragraph in doc.paragraphs:
        text+=paragraph.text+'\n'
    return text