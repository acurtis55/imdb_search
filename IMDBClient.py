import urllib3
from bs4 import BeautifulSoup



class IMDBClient:

    def __init__(self):
        self.url = "http://www.imdb.com/search/title?"


    def __getMovies__(self, searchUrl):

        dataUrl = urllib3.PoolManager().request('GET', searchUrl).data
        soup = BeautifulSoup(dataUrl, "html.parser")

        movieList = soup.findAll('div', attrs={'class': 'lister-item mode-advanced'})

        movieTitles = []

        for divItem in movieList:
            div = divItem.find('div', attrs={'class': 'lister-item-content'})

            header = div.findChildren('h3', attrs={'class':'lister-item-header'})
            movieTitles.append(str((header[0].findChildren('a'))[0].contents[0].encode('utf-8').decode('ascii', 'ignore')))
        return movieTitles

    def searchByReleaseYear(self, releaseYear):

        print("Searching by release year: ", releaseYear)
        searchUrl = self.url + "release_date=" + releaseYear
        return self.__getMovies__(searchUrl)

    def searchByTitle(self, title):

        print("Searching by title: ", title)
        searchUrl = self.url + "title=" + title
        return self.__getMovies__(searchUrl)

    def searchByGenre(self, genre):

        print("Searching by genre: ", genre)
        searchUrl = self.url + "genres=" + genre
        return self.__getMovies__(searchUrl)
