# -*- coding: utf-8 -*-
# Load in data from MovieLens
def loadMovieLens(path= '/data/ml-100k'):
    
    # Get titles
    movies = {}
    for line in open(path + '/u.item'):
        (id,title) = line.split('|')[0:2]
        movies[id] = title
        
    # Load data
    preferences = {}
    for line in open(path+'/u.data'):
        (user,movieid,rating,ts) = line.split('\t')
        preferences.setdefault(user, {})
        preferences[user][movies[movieid]] = float(rating)
    return preferences

# Change ratings from 1-5 scale to Like/Dislike
#def changeRatings():


    