# http://udise.in/Downloads/School%20Directory/A&N.htm
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

for u in urls[:2]:
	r = requests.get(f'http://udise.in/{u}')
	print(r.text)