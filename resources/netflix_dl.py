import csv
import re

import requests
from bs4 import BeautifulSoup

NETFLIX_SERIES_URL = 'https://www.netflix.com/es/browse/genre/83'
NUM_SERIES_TO_DOWNLOAD = 30


class NetflixDownloader:
    def __init__(self, url):
        self.url = url
        self.id = re.search(r'[^/]+$', self.url).group()
        response = requests.get(self.url)
        self.soup = BeautifulSoup(response.text, 'html.parser')
        self._load_serie_fields()
        self._load_seasons()

    @property
    def creators_joined(self):
        return ','.join(self.creators)

    @property
    def starring_joined(self):
        return ','.join(self.starring)

    @property
    def genres_joined(self):
        return ','.join(self.genres)

    def _load_serie_fields(self):
        self.title = self.soup.find('h1', class_='title-title').string.strip()
        self.premiere_year = self.soup.find(
            'span', class_='item-year').string.strip()
        self.age_limit = self.soup.find(
            'span', class_='maturity-number').string.strip()
        self.num_seasons = self.soup.find(
            'span', class_='test_dur_str').string.split()[0].strip()
        self.genres = [
            re.sub(r',[^,]*$', '', e.text)
            for e in self.soup.find_all('span', class_='item-genres')
        ]
        try:
            starring = self.soup.find(
                'div', class_='item-starring').find(
                    'span', class_='title-data-info-item-list').string
            self.starring = re.split(r',\s+', starring)
        except AttributeError:
            self.starring = []
        try:
            creators = self.soup.find(
                'div', class_='item-creators').find(
                    'span', class_='title-data-info-item-list').string
            self.creators = re.split(r',\s+', creators)
        except AttributeError:
            self.creators = []
        try:
            self.twitter_url = self.soup.find(attrs={
                'data-uia': 'social-link-twitter'
            }).get('href')
        except AttributeError:
            self.twitter_url = ''

    def _load_seasons(self):
        episodes_titles = [
            e.string for e in reversed(
                self.soup.find_all('h3', class_='episode-title'))
        ]
        episodes_lengths = [
            e.string for e in reversed(
                self.soup.find_all('span', class_='episode-runtime'))
        ]
        episodes_synopsis = [
            # epsiode-synopsis: error in class name
            e.string for e in reversed(
                self.soup.find_all('p', class_='epsiode-synopsis'))
        ]

        self.seasons, season = [], []
        for title, length, synopsis in zip(episodes_titles, episodes_lengths,
                                           episodes_synopsis):
            episode_number, episode_title = re.match(r'^(\d+)\.\s+(.*)$',
                                                     title.strip()).groups()
            episode_length = length.strip()[:-1]
            try:
                episode_synopsis = synopsis.strip()
            except AttributeError:
                episode_synopsis = ''
            season.insert(
                0, {
                    'title': episode_title,
                    'length': episode_length,
                    'synopsis': episode_synopsis
                })
            if int(episode_number) == 1:
                self.seasons.insert(0, season)
                season = []


response = requests.get(NETFLIX_SERIES_URL)
soup = BeautifulSoup(response.text, 'html.parser')

with open(
        'netflix-series.csv', 'w', newline='') as series_file, open(
            'netflix-seasons.csv', 'w', newline='') as seasons_file:
    series_writer = csv.writer(
        series_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    series_writer.writerow([
        'ID', 'Title', 'Premiere year', 'Age Limit', 'Num. seasons', 'Genres',
        'Starring', 'Creators', 'Twitter URL'
    ])

    seasons_writer = csv.writer(
        seasons_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    seasons_writer.writerow([
        'Serie ID', '#Season', '#Episode', 'Title', 'Length (minutes)',
        'Synopsis'
    ])

    for a in soup.find_all(
            'a',
            class_='nm-collections-title nm-collections-link',
            limit=NUM_SERIES_TO_DOWNLOAD):
        url = a.get('href')
        print(f'Procesando: {url}...')

        ndl = NetflixDownloader(url)

        series_writer.writerow([
            ndl.id, ndl.title, ndl.premiere_year, ndl.age_limit,
            ndl.num_seasons, ndl.genres_joined, ndl.starring_joined,
            ndl.creators_joined, ndl.twitter_url
        ])

        for i, season in enumerate(ndl.seasons):
            for j, episode in enumerate(season):
                seasons_writer.writerow([
                    ndl.id, i + 1, j + 1, episode['title'], episode['length'],
                    episode['synopsis']
                ])
