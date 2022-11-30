import re
import requests
from bs4 import BeautifulSoup

def get_problem_count(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('ul', class_='linksTypeProblem')
    l = s.find_all('li', class_='tab')
    easy,medium,hard = '','',''
    for li in l:
        if('EASY' in li.text):
            easy = re.findall('\((.*?)\)', li.text)
            easy = easy[0]
        if('MEDIUM' in li.text):
            medium = re.findall('\((.*?)\)', li.text)
            medium = medium[0]
        if('HARD' in li.text):
            hard = re.findall('\((.*?)\)', li.text)
            hard = hard[0]
    return easy, medium, hard


# l1,l2,l3 = get_problem_count()
# print(l1,l2,l3)