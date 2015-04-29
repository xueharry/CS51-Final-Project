import os
import math 
import numpy as np
import pandas as pd

def load_data(file_name, npy, path=os.getcwd()+'/data/ml-100k/'):

    # Read in file
    rnames = ['user', 'movie', 'rating', 'timestamp']
    df = pd.read_table(path+file_name, sep='\t', header=None, names=rnames)
    
    # Determine the number of unique users and movies
    num_users = len(np.unique(df[['user']].values))
    num_movies = len(np.unique(df[['movie']].values))

    # Matrix of size num_users x num_movies (rows x cols)
    matrix = [[3 for _ in range(1682)] for _ in range(943)]

    ### Update the average rating for user, normalize to remove bias 

    # Fill in matrix from data
    for index in df.index: 
        user = df['user'][index] 
        movie = df['movie'][index] 
        rating = df['rating'][index] 
        matrix[user-1][movie-1] = rating
        
    # matrix = [[1,2,3,4],[4,3,3,1],[5,5,5,5],[1,4,3,2]]

    if npy==1:
        print('numpy kmeans')
        m = np.array(matrix)
        m.astype(float)
    else:
        print('slow kmeans')
        m=matrix
    
    return m

