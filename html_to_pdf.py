program to convert a .html file into .pdf

pip install pdfkit

import pdfkit

def html_to_pdf(input_html, output_pdf):
    try:
        # Convert HTML to PDF
        pdfkit.from_file(input_html, output_pdf)
        print(f"PDF saved as {output_pdf}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_html = "example.html"  # Path to your HTML file
output_pdf = "output.pdf"    # Desired output PDF file name

html_to_pdf(input_html, output_pdf)
