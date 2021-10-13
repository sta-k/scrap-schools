# http://udise.in/Downloads/School%20Directory/A&N.htm
"""
ERRORS

4 http://udise.in/Downloads/School Directory/Gujarat/2423.pdf
24 http://udise.in/Downloads/School Directory/Gujarat/2419.pdf
Error 24 http://udise.in/Downloads/School Directory/Gujarat/2419.pdf
25 http://udise.in/Downloads/School Directory/Gujarat/2425.pdf
"""

urls = [
	'Downloads/School Directory/A&N.htm', 
	'Downloads/School Directory/AndhraPradesh.htm',
	'Downloads/School Directory/Arunachal.htm',
	'Downloads/School Directory/Assam.htm',
	'Downloads/School Directory/Bihar.htm',
	'Downloads/School Directory/Chandigarh.htm',
	'Downloads/School Directory/Chhattisgarh.htm',
	'Downloads/School Directory/Dadra&NagarHaveli.htm',
	'Downloads/School Directory/Daman&Diu.htm',
	'Downloads/School Directory/Delhi.htm',
	'Downloads/School Directory/Goa.htm',
	'Downloads/School Directory/Gujarat.htm',
	'Downloads/School Directory/Haryana.htm',
	'Downloads/School Directory/Himachal Pradesh.htm',
	'Downloads/School Directory/J&K.htm',
	'Downloads/School Directory/Jharkhand.htm',
	'Downloads/School Directory/Karnataka.htm',
	'Downloads/School Directory/Kerala.htm',
	'Downloads/School Directory/Lakshadweep.htm',
	'Downloads/School Directory/MadhyaPradesh.htm',
	'Downloads/School Directory/Maharashtra.htm',
	'Downloads/School Directory/Manipur.htm',
	'Downloads/School Directory/Meghalaya.htm',
	'Downloads/School Directory/Mizoram.htm',
	'Downloads/School Directory/Nagaland.htm',
	'Downloads/School Directory/Orissa.htm',
	'Downloads/School Directory/Puducherry.htm',
	'Downloads/School Directory/Punjab.htm',
	'Downloads/School Directory/Rajasthan.htm',
	'Downloads/School Directory/Sikkim.htm',
	'Downloads/School Directory/TamilNadu.htm',
	'Downloads/School Directory/Tripura.htm',
	'Downloads/School Directory/Uttarakhand.htm',
	'Downloads/School Directory/UttarPradesh.htm',
	'Downloads/School Directory/WestBengal.htm',
]

import requests
from bs4 import BeautifulSoup # pip install beautifulsoup4
import wget

def get_links():
	
	for u in urls:
		r = requests.get(f'http://udise.in/{u}')
		soup = BeautifulSoup(r.text, 'html.parser')
		options = soup.find_all("option")
		scripts = soup.find_all("script")
		states = [option.get_text() for option in options]

		script_counter = 1
		for unclean_script in scripts:
			clean_data = unclean_script.get_text().split('\n')
			for script in clean_data:
				if 'where_to' in script:
					url = script.split("'")
					if len(url) > 1:
						
						state = u.split('/')[-1][:-4]
						pdf_url = f'http://udise.in/Downloads/School Directory/{url[1]}'
						print(script_counter,pdf_url)
						try:
							wget.download(pdf_url, f'{state}_{states[script_counter]}.pdf')
						except:
							print('Error',script_counter,pdf_url)
						script_counter+=1
if __name__=='__main__':
	get_links()

