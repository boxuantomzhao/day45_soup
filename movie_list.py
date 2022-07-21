from bs4 import BeautifulSoup
import requests
import spotipy

response = requests.get("https://www.imdb.com/list/ls055592025/")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
# print(soup.prettify())
titles = soup.findAll(class_="lister-item-header")

movies = [title.a.getText() for title in titles]
print(movies)
print(len(movies))



