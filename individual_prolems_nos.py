import requests
from bs4 import BeautifulSoup

#gets userurl as an argument and returns the total score of the user from their gfg account
def get_numbers(userurl):
    r = requests.get(userurl)

    soup = BeautifulSoup(r.content, 'html.parser')

    p = soup.find_all('span', class_='score_card_value')
    p = p[1]
    if p is not None:
        return p.text
    else:
        return "-1" # for any error in link