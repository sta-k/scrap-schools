
def pdfparser2(data):
    import PyPDF2
    pdffileobj=open(data,'rb')
     
    #create reader variable that will read the pdffileobj
    read_pdf=PyPDF2.PdfFileReader(pdffileobj)
    page_content=''
    number_of_pages = read_pdf.getNumPages()
    for page_number in range(number_of_pages):   # use xrange in Py2
        page = read_pdf.getPage(page_number)
        page_content += page.extractText()
        # text_file.write(page_content)

    return page_content.split('\n')

def clean_data(text):
    blocks = {}
    current_code = None
    for i,l in enumerate(text):
        if 'Block Code' in l:
            current_code = text[i+2]
            if current_code not in blocks:
                # 12 Block Code & Name: CAMPBELL BAY 350203
                block = {
                    # 'code':clean_data[2],
                    'name':text[i+1],
                    'nschools':text[i-1],
                    'schools':[]
                }
                blocks[current_code] = block


        if len(l) == 11 and l.isdigit(): # 35020300401
            # trying to get name of school
            school = {
                'udise':l,
                'school':text[i+1],
                'village':text[i+2],
            }
            blocks[current_code]['schools'].append(school)
    print(blocks)
if __name__ == '__main__':
    txt = pdfparser2('pdfs/A&N_Nicobars.pdf') 
    clean_data(txt)