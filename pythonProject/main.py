from PyPDF2 import PdfMerger
import csv,os

input_directory = "C:\\116\\Input"
input_csv_file_name = "116.csv"
input_csv_path = os.path.join(input_directory, input_csv_file_name)

with open(input_csv_path, newline="") as sp_numer_file:
    csv_reader = csv.reader(sp_numer_file)
    for row_index, row in enumerate(csv_reader):
        if row_index == 0:
            continue
        sp_numers = [int(value) for value in row[0].split(";")]

        # Open PDF input file and choose a page
        merger = PdfMerger()
        input_pdf_file_name = "116.pdf"
        input_pdf_path = os.path.join(input_directory, input_pdf_file_name)
        input_file = open(input_pdf_path, "rb")
        merger.append(fileobj=input_file, pages=(3+row_index, 4+row_index))

        # Split PDF and save each page to a new file
        output_directory = "C:\\116\\Output\\"
        output_pdf_file_name = f"{tuple(sp_numers[1:2])[0]}.pdf"
        output_pdf_path = os.path.join(output_directory, output_pdf_file_name)
        output = open(output_pdf_path, "wb")
        merger.write(output)

        # Close File Descriptors
        merger.close()
        output.close()
