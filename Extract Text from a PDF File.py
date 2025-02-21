# pip install PyPDF2

import PyPDF2


def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


# Example usage
if __name__ == "__main__":
    pdf_path = "sample.pdf"  # Ensure you have a sample PDF file in your directory
    extracted_text = extract_text_from_pdf(pdf_path)
    print(extracted_text)


# Why? This snippet leverages the PyPDF2 library to extract text from every page of a PDF file. It's perfect for
# automating document processing, enabling quick text analysis, or converting PDF content into a format that can be
# further processed or searched.
