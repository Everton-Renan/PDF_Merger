import os
from pathlib import Path
from time import sleep

import PyPDF2

PDFS_FOLDER = Path(__file__).parent / 'pdfs'
OUTPUT_FOLDER = Path(__file__).parent / 'output'
writer = PyPDF2.PdfWriter()

for pdf in sorted(os.listdir(PDFS_FOLDER)):
    if '.pdf' not in pdf:
        print(f'File type unknown - {pdf}')
        print('The contents of this file will not be added.')
        sleep(1)
        continue

    writer.append(PDFS_FOLDER / pdf)

file_name = str(input('Enter the file name: '))
writer.write(OUTPUT_FOLDER / f'{file_name}.pdf')
writer.close()
