import requests
from bs4 import BeautifulSoup

def get_score(userurl):
    r = requests.get(userurl)

    soup = BeautifulSoup(r.content, 'html.parser')

    s = soup.find('span', class_='score_card_value')

    return s.text