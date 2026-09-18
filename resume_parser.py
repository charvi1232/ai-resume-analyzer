import io
from pypdf import PdfReader
from docx import Document


def extract_text_from_pdf(file_bytes):
    """Extract text from a PDF resume."""
    reader = PdfReader(io.BytesIO(file_bytes))

    text = []

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text.append(page_text)

    return "\n".join(text)


def extract_text_from_docx(file_bytes):
    """Extract text from a DOCX resume."""
    document = Document(io.BytesIO(file_bytes))

    text = []

    for paragraph in document.paragraphs:
        if paragraph.text.strip():
            text.append(paragraph.text)

    return "\n".join(text)


def extract_resume_text(uploaded_file):
    """Extract resume text based on the uploaded file type."""
    file_bytes = uploaded_file.getvalue()
    file_name = uploaded_file.name.lower()

    if file_name.endswith(".pdf"):
        return extract_text_from_pdf(file_bytes)

    elif file_name.endswith(".docx"):
        return extract_text_from_docx(file_bytes)

    else:
        return ""


def clean_resume_text(text):
    """Clean extracted resume text."""
    lines = []

    for line in text.splitlines():
        line = line.strip()

        if line:
            lines.append(line)

    return "\n".join(lines)