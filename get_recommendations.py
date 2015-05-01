# Returns 10 movie recommendations given user's age, gender and occupation
import numpy as np
import preprocessing
import testing
from npkmeans import kmeans

# Run k means
km = kmeans(preprocessing.load_data("u.data", 1), 100)
kmeans_return = km.kCluster()
clusters = kmeans_return[0]
centroids = kmeans_return[1]
testing.calculate(clusters, centroids)

def sim_users_ratings(age, gender, occupation):
    "Calculates similar users, finds those users' centroids, averages centroid ratings and returns a dictionary of sorted movie indexes"
    
    # Load users data
    users = preprocessing.user_load_data("u.user")
    sim_users = []

    # Iterate through users, adding indexes of users with same age, gender and occupation
    for position, user in enumerate(users):
	if (age, gender, occupation) == (user[0], user[1], user[2]):
		sim_users.append(position)
    print sim_users
		
    # Check whether sim_users is empty, if it is, then....
    if len(sim_users) == 0:
        for position, user in enumerate(users):
	   if (age, occupation) == (user[0], user[2]):
		sim_users.append(position)
    print sim_users
			
    if len(sim_users) == 0:
        for position, user in enumerate(users):
	   if (age, gender) == (user[0], user[1]):
		sim_users.append(position)
    print sim_users
       	
    if len(sim_users) == 0:
        for position, user in enumerate(users):
	   if age == user[0]:
		sim_users.append(position)	
    print sim_users

    # Find centroids of similar users 
    user_list = np.array([centroids[clusters[u]] for u in sim_users])
    
    # Average ratings of a list of users, and returns sorted dictionary
    avg = np.mean(user_list, axis=0)
    
    # Convert list to dictionary with index as key and rating as value
    avgdict = dict(enumerate(avg))
    
    # Return list of sorted movie indexes from highest rated to lowest rated
    return sorted(avgdict, key=avgdict.get, reverse=True)


def top_movies(n,movies):
    "Returns the top n movies"
    
    # Load movie data
    movie_table = preprocessing.movie_load_data("u.item")
    
    top_ten = [movies[m] for m in xrange(0,n)]
    top_movies = [movie_table[m][1] for m in top_ten]
    
    return top_movies
    
    
    
    
    

    
    





