import PyPDF2

def extract_text(file, pasted_text):
    if pasted_text:
        return pasted_text
    if file is not None:
        if file.name.endswith('.pdf'):
            pdf_reader = PyPDF2.PdfReader(file)
            return "\n".join([page.extract_text() for page in pdf_reader.pages])
        elif file.name.endswith('.txt'):
            return file.read().decode('utf-8')
    return ""
