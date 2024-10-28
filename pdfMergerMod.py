import PyPDF2
import os

# defines the path of image folders
path = './files'
pathOut = '/combinedFiles'

merger = PyPDF2.PdfMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        print(file)
        merger.append(file)
# writes the file into the 'combinedFiles' folder
merger.write(f'.{pathOut}/combined.pdf')
