import pikepdf
import os

pdf_loc = 'aadhaar.pdf'
pdf_pass = 'ABHA13121886'

pdf = pikepdf.open(pdf_loc, password=pdf_pass)

print("\nProcessing...\n")

pdf_save = 'unlock' + os.path.basename(pdf_loc)

pdf.save(os.path.join(os.path.dirname(pdf_loc), pdf_save))

print("The password successfully removed from the PDF")
print("\aLocation: " + pdf_loc + '\\' + pdf_save)
