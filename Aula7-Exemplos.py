# import json
# import requests


# json_response=requests.get("https://feeds.citibikenyc.com/stations/stations.json")
# print(type(json_response.text))
# bike_dict=json.loads(json_response.text)
# print(type(bike_dict))
# print(bike_dict['stationBeanList'][0])

# Fazer exemplo infinito e none

# PDF em Pyton
import PyPDF2

# pdfFileObj=open('example.pdf','rb')  #Creating a pdf File object  PS:o caminho n pode ser muito grande
#
# pdfReader=PyPDF2.PdfFileReader(pdfFileObj) #Creating a pdf Reader object
#
# print(pdfReader.numPages) #Printing number ofprint pages in pdf file
#
# pageObj=pdfReader.getPage(0) #Creating a page object
#
# print(pageObj.extractText()) #Extracting text from page
#
# pdfFileObj.close() #Closing a pdf File object

#  Rotação de páginas PDF
# def PDFrotate(origFileName,newFileName,rotation):
#     pdfFileObj=open(origFileName,'rb')
#     pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
#     pdfWriter=PyPDF2.PdfFileWriter()
#     for page in range(pdfReader.numPages):
#         pageObj=pdfReader.getPage(page)
#         pageObj.rotateClockwise(rotation)
#         pdfWriter.addPage(pageObj)
#     newFile=open(newFileName,'wb')
#     pdfWriter.write(newFile)
#     pdfFileObj.close()
#     newFile.close()
# def main():
#     origFileName='example.pdf'
#     newFileName='example_rotated.pdf'
#     rotation=270
#     PDFrotate(origFileName,newFileName,rotation)
# if __name__=="__main__":
#     main()

#  Fusão de PDF's
# def PDFmerge(pdfs,output):
#     pdfMerge=PyPDF2.PdfFileMerger()
#     for pdf in pdfs:
#         with open(pdf,'rb') as f:
#             pdfMerge.append(f)
#
#     with open(output,'wb') as f:
#         pdfMerge.write(f)
# def main():
#     pdfs=['example.pdf','example_rotated.pdf','example_combined.pdf']
#     output='example_combined3.pdf'
#     PDFmerge(pdfs=pdfs,output=output)
# if __name__ == '__main__':
#     main()

#  Dividir PDF's
# def PDFsplit(pdf,splits):
#     pdfFileObj=open(pdf,'rb')
#     pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
#     start=0
#     end=splits[0]
#     for i in range(len(splits)+1):
#         pdfWriter=PyPDF2.PdfFileWriter()
#         outputpdf=pdf.split('.pdf')[0]+str(i)+'.pdf'
#         for page in range(start,end):
#             pdfWriter.addPage(pdfReader.getPage(page))
#         with open(outputpdf,'wb') as f:
#             pdfWriter.write(f)
#         start=end
#         try:
#             end=splits[i+1]
#         except IndexError:
#             end=pdfReader.numPages
#     pdfFileObj.close()
# def main():
#     pdf='example.pdf'
#     splits = [2,4]
#     PDFsplit(pdf,splits)
# if __name__ =="__main__":
#     main()

# Marca de Agua

def add_watermark(wmFile,pageObj):
    wmFileObj=open(wmFile,'rb')
    pdfReader=PyPDF2.PdfFileReader(wmFileObj)
    pageObj.mergePage(pdfReader.getPage(0))
    wmFileObj.close()
    return pageObj
def main():
    mywatermark='watermark.pdf'
    origFileName='example.pdf'
    newFileName='example_watermark.pdf'
    pdfFileObj=open(origFileName,'rb')
    pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
    pdfWriter=PyPDF2.PdfFileWriter()
    for page in range(pdfReader.numPages):
        wmpageObj=add_watermark(mywatermark,pdfReader.getPage(page))
        pdfWriter.addPage(wmpageObj)
    newFile=open(newFileName,'wb')
    pdfWriter.write(newFile)
    pdfFileObj.close()

if __name__=="__main__":
    main()
