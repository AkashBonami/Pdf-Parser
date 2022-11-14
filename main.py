from extract_name import name
from PyPDF2 import PdfFileReader,PdfFileWriter
from generator import Parser

file_path = '746860-1.pdf'
file_name = name(file_path)
pdf = PdfFileReader(file_path)
Parser(file_name,pdf)