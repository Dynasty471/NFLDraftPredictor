import requests
from bs4 import BeautifulSoup

BASE_URL = 'http://www.pro-football-reference.com'


def parse_player(link):
    r = requests.get(link)
    rsoup = BeautifulSoup(r.text, 'html.parser')
    stats = {}
#    get_measurements(rsoup, stats)
    get_stats(rsoup, stats)

def get_stats(soup, stats):
    seasons = soup.find_all('tr')	
    for season in seasons:
        stats = season.find_all('td')
        for stat in stats:
            # TODO Do we want to parse for position here and then create
            # separate functions to parse each position?
            print(stat.get('data-stat'))
            
            print(stat.string)		

def get_measurements(soup, stats):
    for span_tag in soup.find_all('span'):
        span_property = span_tag.get('itemprop')
        if span_property == "height":
            print("Height: " + span_tag.string)
            stats['Height'] = span_tag.string
        elif span_property == "weight":
            print("Weight: " + span_tag.string)
            stats['Weight'] = span_tag.string

# Go through the draft table, and pull the player college stats page and
# the draft position.
def generate_dataset():
    r = requests.get('http://www.pro-football-reference.com/years/2015/draft.htm')
    rsoup = BeautifulSoup(r.text, 'html.parser')
    # Isolate each individual player row.
    player_rows = rsoup.find_all('tr')
    for player in player_rows:
        # Go through each column of each row.
        columns = player.find_all('td')
        for column in columns:
            if column.get('data-stat') == "college_link":
                link = player.strong.a.get('href')
                link = BASE_URL + link
                parse_player(link)

if __name__ == "__main__":
    generate_dataset()
