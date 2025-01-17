import pandas as pd
import random
import subprocess

dMovies = pd.read_csv('output/dfMovies.csv')
dTomatoe = pd.read_csv('output/dfTomatoe.csv')
listgenres = ['drama', 'horror', 'comedy', 'thriller', 'romance']


# Check the user write right Genre

def checkGenre(genre):
    while True:
        if genre in listgenres:
            return genre
            break
        else:
            genre=input("Please choose a movie genre: drama, horror, comedy, thriller or romance ")

# Choice a random movie from rottentomatoes

def chooseGenre(genre):
    dtlist=dTomatoe[genre].tolist()
    dflist=dMovies['title'].tolist()
    while True:
        movie = random.choice(dtlist)
        if movie in dflist:
            print ("My recommendation is " + movie.upper())
            return movie
            break
        else:
            continue

# Get the info of the random movie

def showMovie(movie):
    import pandas as pd
    moviereport = (dMovies[dMovies['title'] == movie])
    return moviereport

# Check if you can reproduce the sound

def soundChecker():
    answer = input("Do you are on Ubuntu with Espeak installed? Press Y or N? ")
    answer = answer.upper()
    mailname = input("Please write your name ")
    if answer == 'Y':
       text = '" {}, YOU HAVE, AN EMAIL."'.format(mailname)
       subprocess.call('espeak -vF4 '+text, shell=True)
    else:
        print("Ohh...{} You should!:__(".format(mailname))