from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get("https://www.imdb.com/chart/top/")

soup = BeautifulSoup(page.content,"html.parser")

imdb_Top250 = soup.find(class_="lister-list")
movie_list = imdb_Top250.find_all(class_="titleColumn")

rating_List=imdb_Top250.find_all(class_='imdbRating')
year_list=imdb_Top250.find_all(class_="titleColumn")
movieRatings=[]
movieNames=[]
movieYears=[]
for names in movie_list:
  names = names.find('a').get_text()
  movieNames.append(names)
for rates in rating_List:
  rates = rates.find('strong').get_text()
  movieRatings.append(rates)
for years in year_list:
  years = years.find('span').get_text()
  movieYears.append(years)

imdbTable= pd.DataFrame(
  {
    "Title": movieNames,
    "Year": movieYears,
    "Rating": movieRatings
  }
)
print(imdbTable)

totalMovieRating=0
for rating in movieRatings:
  rating = float(rating)
  totalMovieRating += rating
  averageScore = totalMovieRating / len(movieRatings)
print("Average rating of all: ",(round(averageScore,3)))  

