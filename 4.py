from bs4 import BeautifulSoup
import requests


def get_followers(username):
	pass

def get_repositories(username):
	response = requests.get('https://github.com/' + username + '?tab=repositories')
	soup = BeautifulSoup(response.text, 'html.parser')
	return len(soup.find_all("a", {"itemprop": "name codeRepository"}))


def get_languages(username):
	pass


print(get_repositories('torvalds'))