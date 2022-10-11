
#THIS CODE IS STILL UNDER CONSTRUCTION AND HAS NO PORPOSE CURRENTLY

import requests
import pandas as pd #needed for table scraping
from bs4 import BeautifulSoup

r = requests.get('https://auth.geeksforgeeks.org/college/rcc-institute-of-information-technology-rcciit-kolkata/')

soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find('div', class_='institute_student_table_div center-align')

print(s)