from docx import Document
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_ORIENT

# Create the document
doc = Document()

# Set Orientation to Landscape
section = doc.sections[0]
new_width, new_height = section.page_height, section.page_width
section.orientation = WD_ORIENT.LANDSCAPE
section.page_width = new_width
section.page_height = new_height

# Add Title
title = doc.add_heading('READIUM SCHOOL D.I. KHAN', 0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
subtitle = doc.add_paragraph('FINAL TERM TIME TABLE (REVISED)')
subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER

# Define the table data matrix exactly as requested
# Header Row
headers = ["Time", "Per", "PG A", "PG B", "KG", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th"]

# Data Rows
rows_data = [
    # Row 1: 8:45-9:20
    ["8:45-9:20", "1", "Urdu\nMiss Kanwal", "English\nMiss Kanwal", "Free", "English\nSir Fayal", "Islamiat\nSir Hasnain", "Math\nMiss Shazia", "Science\nMiss Kubra", "S.S\nSir Saqib", "English\nSir Huziafa", "Urdu\nSir Javed"],
    
    # Row 2: 9:20-9:55
    ["9:20-9:55", "2", "Free", "English\nSir Fayal", "Math\nSir Fayal", "S.S\nMiss Malaika", "English\nMiss Malaika", "English\nSir Huziafa", "S.S\nSir Saqib", "Math\nMiss Shazia", "Islamiat\nSir Hasnain", "Islamiat\nSir Hasnain"],
    
    # Row 3: 9:55-10:30 (KG correction: Eng/Faryal)
    ["9:55-10:30", "3", "Free", "Urdu\nMiss Kanwal", "English\nMiss Faryal", "English\nSir Fayal", "Science\nMiss Kubra", "Urdu\nMiss Malaika", "English\nSir Huziafa", "Urdu\nSir Javed", "Math\nMiss Shazia", "History\nSir Saqib"],
    
    # Row 4: 10:30-11:05 (Many corrections here: 2nd Urdu/Faryal, 3rd SS/Saqib, 5th Isl/Hasnain, 6th Sci/Kubra, 7th Eng/Huzaifa)
    ["10:30-11:05", "4", "Math\nMiss Kanwal", "Free", "Free", "Science\nMiss Shazia", "Urdu\nMiss Faryal", "S.S\nSir Saqib", "Islamiat\nSir Hasnain", "Islamiat\nSir Hasnain", "Science\nMiss Kubra", "English\nSir Huzaifa"],
    
    # Break
    ["11:05-11:20", "BRK", "BREAK", "BREAK", "BREAK", "BREAK", "BREAK", "BREAK", "BREAK", "BREAK", "BREAK", "BREAK"],
    
    # Row 5: 11:20-11:55 (Period 5)
    ["11:20-11:55", "5", "Free", "Math\nMiss Kanwal", "Activity\nSir Javed", "Urdu\nSir Fayal", "S.S\nMiss Malaika", "Science\nMiss Kubra", "Islamiat\nSir Hasnain", "English\nSir Huziafa", "History\nSir Saqib", "Science\nMiss Kubra"],
    
    # Row 6: 11:55-12:30 (Period 6) (Corrections: PG B Free, 1st Eng/Malaika, 2nd Math/Saqib, 3rd Isl/Hasnain, 4th Math/Shazia, 5th Sci/Kubra)
    ["11:55-12:30", "6", "Activity\nMiss Kanwal", "Free", "Eng\nMiss Malaika", "English\nMiss Malaika", "Math\nSir Saqib", "Islamiat\nSir Hasnain", "Math\nMiss Shazia", "Science\nMiss Kubra", "Urdu\nSir Javed", "Science\nMiss Kubra"],
    
    # Row 7: 12:30-12:50 (Period 7) (Corrections: PG A Activity/Kubra, 2nd Gram/Malaika, 3rd Gram/Shazia, 4th Free, 5th Free, 6th Gram/Saqib, 7th Free)
    ["12:30-12:50", "7", "Activity\nMiss Kubra", "Activity\nSir Hasnain", "Grammar\nSir Fayal", "Grammar\nMiss Malaika", "Grammar\nMiss Malaika", "Grammar\nMiss Shazia", "Free", "Free", "Grammar\nSir Saqib", "Free"]
]

# Create Table
table = doc.add_table(rows=1, cols=len(headers))
table.style = 'Table Grid'

# Add Headers
hdr_cells = table.rows[0].cells
for i, header in enumerate(headers):
    hdr_cells[i].text = header
    hdr_cells[i].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    hdr_cells[i].paragraphs[0].runs[0].font.bold = True

# Add Rows
for row_data in rows_data:
    row_cells = table.add_row().cells
    for i, cell_text in enumerate(row_data):
        row_cells[i].text = cell_text
        for paragraph in row_cells[i].paragraphs:
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            if row_data[0] == "11:05-11:20": # Bold the break row
                 for run in paragraph.runs:
                     run.font.bold = True

# Save
file_path = "/mnt/data/Revised_Readium_School_Timetable.docx"
doc.save(file_path)
file_path