#SCRAPPING THROUGH PYTHON
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import numpy
url = 'https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

movie_name = []
year = []

movie_data = soup.findAll('div', attrs={'class': 'lister-item mode-advanced'})
for store in movie_data:
    name = store.h3.a.text
    movie_name.append(name)
    year_of_release = store.h3.find('span', class_='lister-item-year text-muted unbold').text.replace('(', '').replace(')', '')
    year.append(year_of_release)

movie_titles = movie_name

print(movie_name,year)
