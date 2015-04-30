# Returns 10 movie recommendations given user's age, gender and occupation
import numpy as np
import preprocessing
from npkmeans import kmeans

# Run k means
km = kmeans(preprocessing.load_data("u.data", 1), 100)
kmeans_return = km.kCluster()
clusters = kmeans_return[0]
centroids = kmeans_return[1]

def get_sim_users(age, gender, occupation):
    "Returns list of indexes of users with same age, same gender and same occupation"
    users = preprocessing.user_load_data("u.user")
    sim_users = []

    # Iterate through users, adding indexes of users with same age, gender and occupation"
    for position, user in enumerate(users):
	if (age, gender, occupation) == (user[0], user[1], user[2]):
		sim_users.append(position)

    return sim_users
    
def get_sim_users_centroids(users):
    "Returns list of centroids of users"
    return np.array([centroids[clusters[u]] for u in users])
    
def average_ratings(users_list):
    "Averages ratings of a list of users, returns sorted dictionary"
    avg = np.mean(users_list, axis=0)
    # Convert list to dictionary with index as key and rating as value
    avgdict = dict(enumerate(avg))
    # Return list of sorted movie indexes from highest rated to lowest rated
    return sorted(avgdict, key=avgdict.get, reverse=True)

def top_movies(movies):
    top_ten = [movies[m] for m in xrange(0,9)]
    print top_ten
    movie_table = preprocessing.movie_load_data("u.item")
    top_movies = [movie_table[m][1] for m in top_ten]
    return top_movies
    
    
    
    
    

    
    





