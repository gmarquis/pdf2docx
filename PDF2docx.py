from pdf2docx import Converter
pdf_file = '../../Documents/AdobeDocument.pdf'
docx_file = '../../Documents/ConvertedDocument.docx'
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()