import os
import PyPDF2

def read_and_modify_pdf():
    filename = input("WDPA_Manual.pdf): ").strip()

    if not filename.lower().endswith('.pdf'):
        print("Error: The file must have a .pdf extension.")
        return

    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return

    try:
        with open(filename, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""

            for i, page in enumerate(reader.pages):
                try:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
                except Exception as e:
                    print(f"Warning: Could not read page {i + 1}: {e}")

    except Exception as e:
        print(f"Error opening file: {e}")
        return

    if not text.strip():
        print("Error: No readable text found in the PDF.")
        return

    modified_text = text.upper()
    new_filename = "modified_" + os.path.splitext(filename)[0] + ".txt"

    try:
        with open(new_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(modified_text)
        print(f"Modified content written to '{new_filename}'.")
    except Exception as e:
        print(f"Error writing to file: {e}")

read_and_modify_pdf()
