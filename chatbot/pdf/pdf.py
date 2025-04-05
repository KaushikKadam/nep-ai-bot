from fpdf import FPDF

# Create PDF object
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Set title
pdf.set_font('Arial', 'B', 16)
pdf.cell(200, 10, 'Frequently Asked Questions (FAQs) - National Education Policy (NEP) 2020', ln=True, align='C')

# Add a line break
pdf.ln(10)

# Set font for the content
pdf.set_font('Arial', '', 12)

# FAQ list
faq_list = [
    
]

# Add FAQs to the PDF
for question, answer in faq_list:
    pdf.multi_cell(0, 10, f"{question}\n{answer}\n")

# Save the PDF to a file
output_file = "NEP_2020_FAQs.pdf"
pdf.output(output_file)

print(f"PDF has been created: {output_file}")
