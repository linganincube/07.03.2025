import re
from pypdf import PdfReader
import pandas as pd


def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file using PyPDF.
    """
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


def parse_text_to_table(text):
    """
    Parses the extracted text into a structured table format.
    This function assumes that rows are separated by newlines and columns by spaces/tabs.
    Modify this function based on your PDF's structure.
    """
    # Split the text into lines
    lines = text.split('\n')

    # Parse each line into columns (assuming space-separated values)
    data = []
    for line in lines:
        # Remove extra spaces and split by whitespace
        row = re.split(r'\s{2,}', line.strip())
        if row:  # Ignore empty rows
            data.append(row)

    return data


def save_to_excel(data, excel_path):
    """
    Saves the parsed data into an Excel file.
    """
    # Create a DataFrame from the parsed data
    df = pd.DataFrame(data[1:], columns=data[0])  # Assuming the first row is the header

    # Save the DataFrame to an Excel file
    df.to_excel(excel_path, index=False)
    print(f"Data successfully saved to {excel_path}")


def pdf_to_excel(pdf_path, excel_path):
    """
    Converts a PDF file to an Excel file.
    """
    # Step 1: Extract text from the PDF
    print("Extracting text from PDF...")
    text = extract_text_from_pdf(pdf_path)

    # Step 2: Parse the text into a table format
    print("Parsing text into table format...")
    data = parse_text_to_table(text)

    # Step 3: Save the parsed data to an Excel file
    print("Saving data to Excel...")
    save_to_excel(data, excel_path)


# Example usage
if __name__ == "__main__":
    pdf_file = "C:lncube\Documents\binga_branch.pdf"  # Replace with your PDF file path
    excel_file = "C:lncube\Documents\binga_branch.xlsx"  # Replace with your desired Excel file path
    pdf_to_excel(pdf_file, excel_file)