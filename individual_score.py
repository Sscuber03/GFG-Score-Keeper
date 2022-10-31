import requests
from bs4 import BeautifulSoup

#gets userurl as an argument and returns the total score of the user from their gfg account
def get_score(userurl):
    r = requests.get(userurl)

    soup = BeautifulSoup(r.content, 'html.parser')

    s = soup.find('span', class_='score_card_value')

    if s is not None:
        return s.text
    else:
        return "-1" # for any error in link