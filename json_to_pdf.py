import json
from fpdf import FPDF

# Function To Convert JSON To Plaintext String
def json_to_plaintext(json_obj, indent=0):
    
    plaintext = ""
    indent_str = " " * indent

    if isinstance(json_obj, dict):
        for key, value in json_obj.items():
            plaintext += f"{indent_str}{key}: "
            if isinstance(value, (dict, list)):
                plaintext += "\n" + json_to_plaintext(value, indent + 2)
            else:
                plaintext += f"{value}\n"
    elif isinstance(json_obj, list):
        for item in json_obj:
            plaintext += indent_str + "- " + json_to_plaintext(item, indent + 2)
    else:
        plaintext += f"{json_obj}\n"

    return plaintext

# Function To Save A Plaintext String As A PDF
def text_to_pdf(text, pdf_file_path):
    
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Split The Text By Lines And Add TO PDF
    for line in text.splitlines():
        pdf.multi_cell(0, 10, line)

    # Save The Generated PDF To The Specified File Path
    pdf.output(pdf_file_path)

# Main Function To Read JSON, Convert To Plaintext, And Write To PDF
def json_file_to_pdf(json_file_path, pdf_file_path):
    
    # Read the JSON File
    with open(json_file_path, 'r') as file:
        json_data = json.load(file)

    # Convert JSON Data To Plaintext String
    plaintext = json_to_plaintext(json_data)

    # Convert The Plaintext String To A PDF
    text_to_pdf(plaintext, pdf_file_path)

# Main Program To Demonstrate Usage
if __name__ == '__main__':

    # Example Usage
    json_file_path = "./json/lettuce.json"
    pdf_file_path = "./pdf/lettuce.pdf"

    json_file_to_pdf(json_file_path, pdf_file_path)
    print(f"PDF saved as {pdf_file_path}")