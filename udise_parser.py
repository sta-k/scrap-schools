# palakkad district

fp = open('/home/suhail/Desktop/work/schools/pdfs/udise.txt','r')
loopcounter = 0
blocks = {}
current_code = None

for l in fp.readlines():
    # if loopcounter == 20: break

    # trying to get sub district
    if 'Block Code' in l: 
        # ['&', 'Name:', '320601', 'AGALI', 'Total', 'Schools', 'in', 'this', 'block', ':', '58']
        clean_data = l.split('Block Code')[1].split()
        
        current_code = clean_data[2]
        if current_code not in blocks:
            block = {
                # 'code':clean_data[2],
                'name':clean_data[3],
                'nschools':clean_data[10],
                'schools':[]
            }
            blocks[current_code] = block


    # get udise
    # ['1', '32060100116', 'AIS', 'KARUVARA',
    clean_data = l.split()
    if len(clean_data) < 2: continue

    if len(clean_data[1]) == 11:
        # trying to get name of school
        items = l.split(clean_data[1])[1].split('  ')
        school = {
            'udise':clean_data[1],
            'school':items[2],
            # 'village':l.split(items[2])[1].split()
        }
        blocks[current_code]['schools'].append(school)

    loopcounter+=1
print(blocks)
# for key,value in blocks.items():
#     print(key, value['name'], value['nschools'])
#     for school in value['schools']:
#         print(school)
