from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import os
import PyPDF2

from schools.models import State,District, SubDistrict, EduDistrict, School

def pdfparser2(data):
    pdffileobj=open(data,'rb')
     
    #create reader variable that will read the pdffileobj
    read_pdf=PyPDF2.PdfFileReader(pdffileobj)
    page_content=''
    number_of_pages = read_pdf.getNumPages()
    for page_number in range(number_of_pages):   # use xrange in Py2
        page = read_pdf.getPage(page_number)
        page_content += page.extractText()
        # text_file.write(page_content)
        # break

    return page_content.split('\n')

def clean_data(text, dist=None):
    blocks = {}
    current_code = None
    subdist = None
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
                subdist,_ = SubDistrict.objects.get_or_create(
                    code = current_code,
                    defaults={
                        'name': block['name'],
                        'no_schools':block['nschools'],
                        'district':dist
                    })


        if len(l) == 11 and l.isdigit(): # 35020300401
            # trying to get name of school
            school = {
                'udise':l,
                'school':text[i-1],
                'village':text[i+1],
            }
            blocks[current_code]['schools'].append(school)
        
            edist,_=EduDistrict.objects.get_or_create(name=school['village'],defaults={'subdistrict':subdist})

            School.objects.get_or_create(udise=school['udise'],
            defaults={'name':school['school'],'edudistrict':edist})

    # print(blocks)

def save_db():
    folder = '/home/suhail/github/scrap-schools'
    _, _, folder_files = next(os.walk(os.path.join(folder, 'pdfs')))
    for fp in folder_files:
        # print (fp)
        state_dist = fp.rsplit('_',1)
        data = {
            'state': state_dist[0].replace(' ','_'),
            'dist':state_dist[1].replace('.pdf','').replace(' ','_'),
        }
        s,created = State.objects.get_or_create(name=data['state'])
        d, d_created = District.objects.get_or_create(name=data['dist'], defaults={'state':s})
        if created:
            print('School created:'+data['state'])
        
        if d_created:
            print('District Created:'+data['dist'])
            # Jhalawar or 

        if data['dist'] == 'Jhalawar':
            print('Jhalwar')
            txt = pdfparser2(f'{folder}/pdfs/{fp}') 
            clean_data(txt,d)
        elif d_created:
            txt = pdfparser2(f'{folder}/pdfs/{fp}') 
            clean_data(txt,d)
        else:
            print('skipping')
        # break


    
def home(request):
    if request.POST: 
        # return redirect('schools:districts')
        save_db()
        return HttpResponse('schools:districts')
    total = School.objects.count()
    return render(request, 'home.html', {'total':total})
