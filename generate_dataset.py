import requests
from bs4 import BeautifulSoup

BASE_URL = 'http://www.pro-football-reference.com'

def parse_player(link):
	r = requests.get(link)
	rsoup = BeautifulSoup(r.text, 'html.parser')
	seasons = rsoup.find_all('tr')
	
	for season in seasons:
		stats = season.find_all('td')
		for stat in stats:
			print(stat.get('data-stat'))
			print(stat.string)		

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
	

