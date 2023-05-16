"""Dada una pila de películas de las que se conoce su título, estudio cinematográfico y año de estreno, desarrollar las funciones necesarias para resolver las siguientes actividades:

a. mostrar los nombre películas estrenadas en el año 2014
b. indicar cuántas películas se estrenaron en el año 2018
c. mostrar las películas de Marvel Studios estrenadas en el año 2016"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("algoritmos_2023"))))

from operator import itemgetter
from classStack import Stack

stack = Stack()

movies = [
  {
    "title": "Guardians of the Galaxy",
    "studio": "Marvel Studios",
    "release_date": "2014"
  },
  {
    "title": "Deadpool",
    "studio": "20th Century Fox",
    "release_date": "2016"
  },
  {
    "title": "Captain America: Civil War",
    "studio": "Marvel Studios",
    "release_date": "2016"
  },
  {
    "title": "Doctor Strange",
    "studio": "Marvel Studios",
    "release_date": "2016"
  },
  {
    "title": "Star Wars: The Last Jedi",
    "studio": "Lucasfilm",
    "release_date": "2017"
  },
  {
    "title": "Black Panther",
    "studio": "Marvel Studios",
    "release_date": "2018"
  },
  {
    "title": "Avengers: Infinity War",
    "studio": "Marvel Studios",
    "release_date": "2018"
  }
]

def fillStack():
    for i in movies:
        stack.push(i)

def searchMovie(searchParams):
    fillStack()

    getParams = itemgetter("title", "studio", "release_date")
    title, studio, release_date = getParams(searchParams)

    movies = []

    while stack.size() > 0:
        movie = stack.pop()

        if ((title == "" or (movie["title"] == title)) and (studio == "" or (movie["studio"] == studio)) and (release_date == "" or (movie["release_date"] == release_date))):
            movies.append(movie["title"])

    return movies

print(searchMovie({ "title": "", "studio": "", "release_date": "2014" }))
print(searchMovie({ "title": "", "studio": "", "release_date": "2018" }))
print(searchMovie({ "title": "", "studio": "Marvel Studios", "release_date": "2016" }))


