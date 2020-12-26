import requests
import random
from bs4 import BeautifulSoup


class Movie:
    URL = 'https://www.imdb.com/search/title/?title_type=feature&release_date=2019-01-01,2020-12-31'
    MOVIES = list()

    def __init__(self, from_year, to_year):
        self.from_year = from_year
        self.to_year = to_year
        self.URL = f'https://www.imdb.com/search/title/?title_type=feature&release_date={from_year},{to_year}'
        self.response = requests.get(self.URL).content
        self.soup = BeautifulSoup(self.response, 'html.parser')
        self.collect_movies()

    def collect_movies(self):
        movies = self.soup.select(
            'html body#styleguide-v2.fixed div#wrapper div#root.redesign div#pagecontent.pagecontent div#content-2-wide.redesign div#main div.article div.lister.list.detail.sub-list div.lister-list div.lister-item.mode-advanced div.lister-item-content')

        for movie in movies:
            self.MOVIES.append({'movie': movie.select('h3 a')[0].text,
                                'genre': movie.select('p.text-muted span.genre')[0].text.strip(),
                                'ratings': movie.select('div.ratings-bar div.inline-block strong')[0].text}
                               )

    def get_all_movies(self):
        return self.MOVIES

    def get_random_movie(self):
        movie = random.choice(self.MOVIES)
        return movie
