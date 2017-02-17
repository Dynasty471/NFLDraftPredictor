import requests
from bs4 import BeautifulSoup

BASE_URL = 'http://www.pro-football-reference.com'

def get_measurements(soup, stats):
    for span_tag in soup.find_all('span'):
        span_property = span_tag.get('itemprop')
        if span_property == "height":
            print("Height: " + span_tag.string)
            stats['Height'] = span_tag.string
        elif span_property == "weight":
            print("Weight: " + span_tag.string)
            stats['Weight'] = span_tag.string

def parse_player(link):
    r = requests.get(link)
    rsoup = BeautifulSoup(r.text, 'html.parser')
    stats = {}
    get_measurements(rsoup, stats)
    #	stats = rsoup.find_all('td')
def generate_dataset():
    r = requests.get('http://www.pro-football-reference.com/years/2015/draft.htm')
    rsoup = BeautifulSoup(r.text, 'html.parser')
    player_rows = rsoup.find_all('tr')
    for player in player_rows:
        if player.strong:
            link = player.strong.a.get('href')
            link = BASE_URL + link
            parse_player(link)

if __name__ == "__main__":
    generate_dataset()
