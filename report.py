from fpdf import FPDF
import suggestions as s

def create_pdf(entries, filename):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Carbon Footprint Analysis Report", ln=True, align="C")
    pdf.ln(5)
    
    for i, entry in enumerate(entries):
        pdf.cell(200, 10, txt=f"Entry {i+1}:", ln=True, align="L")
        pdf.cell(200, 10, txt=f"Total Carbon Footprint: {sum(entry)} metric tons CO2 equivalent", ln=True, align="L")
        pdf.multi_cell(0, 10, txt=f"Energy Usage Suggestion:\n{s.energy_suggestion(entry[0])}")
        pdf.multi_cell(0, 10, txt=f"Waste Generation Suggestion:\n{s.waste_suggestion(entry[1])}")
        pdf.multi_cell(0, 10, txt=f"Business Travel Suggestion:\n{s.travel_suggestion(entry[2])}")
        pdf.ln(0)
        
        # Embed charts as images in the PDF
        pdf.image(f"charts/entry_{i+1}_All_input_data_results.png", x=10, y=pdf.get_y() + 10, w=150)
        pdf.ln(180)
    
    pdf.add_page()
    pdf.image("charts/total_carbon_footprint.png", x=10, y=pdf.get_y() + 10, w=180)
    pdf.ln(110)
    
    # Embed bar chart for total carbon footprint by entry
    pdf.image("charts/total_carbon_footprint_by_entry.png", x=10, y=pdf.get_y() + 10, w=180)
    pdf.ln(110)
    
    pdf.output(f"reports/{filename}")
