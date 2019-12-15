import PyPDF2 as pdf

pdfFile = open('meetingminutes1.pdf', 'rb')
reader = pdf.PdfFileReader(pdfFile)
pageNum = reader.numPages # view number of pages
print(pageNum)


page = reader.getPage(0) # read pdf
read = page.extractText()
print(read)

#read multiple pages

for pageNum in range(reader.numPages):
	print(reader.getPage(pageNum).extractText())


# combibe 2 pdf file

pdf1File = open('meetingminutes1.pdf','rb')
pdf2File = open('meetingminutes2.pdf','rb')

reader1 = pdf.PdfFileReader(pdf1File)
reader2 = pdf.PdfFileReader(pdf2File)


writer = pdf.PdfFileWriter()
for pageNum in range(reader1.numPages):
	page = reader1.getPage(pageNum)
	writer.addPage(page)

	
for pageNum in range(reader2.numPages):
	page = reader2.getPage(pageNum)
	writer.addPage(page)

	
outputFile = open('combineminutes.pdf', 'wb') # new pdf
writer.write(outputFile)

outputFile.close()
pdf1File.close()
pdf2File.close()
