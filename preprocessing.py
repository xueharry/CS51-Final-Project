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
    matrix = [[3 for _ in range(num_movies)] for _ in range(num_users)]

    # Fill in matrix from data
    for index in df.index: 
        user = df['user'][index] 
        movie = df['movie'][index] 
        rating = df['rating'][index] 
        matrix[user-1][movie-1] = rating

    # Check for which version of kmeans to use
    if npy == 1:
        print('numpy kmeans')
        m = np.array(matrix)
        m.astype(float)
    else:
        print('slow kmeans')
        m = matrix
    
    return m
    

def testing_load_data(file_name, path=os.getcwd()+'/data/ml-100k/'):

    # Read in file
    rnames = ['user', 'movie', 'rating', 'timestamp']
    df = pd.read_table(path+file_name, sep='\t', header=None, names=rnames)

    # Matrix of size num_users x num_movies (rows x cols)
    matrix = [[0 for _ in range(1682)] for _ in range(943)]

    # Fill in matrix from data
    for index in df.index: 
        user = df['user'][index] 
        movie = df['movie'][index] 
        rating = df['rating'][index] 
        matrix[user-1][movie-1] = rating

    # Convert to numpy array
    m = np.array(matrix)
    m.astype(float)

    return m


def user_load_data(file_name, path=os.getcwd()+'/data/ml-100k/'):

    # Read in file 
    rnames = ['age', 'gender', 'occupation', 'zipcode']
    df = pd.read_csv(path+file_name, delimiter = '|', header=None, names = rnames)
    
    # Convert to list
    dflist = df.values.tolist()
    
    return dflist


def movie_load_data(file_name, path=os.getcwd()+'/data/ml-100k/'):

    # Read in file
    df = pd.read_csv(path+file_name, delimiter = '|', header=None)

    # Convert to list
    dflist = df.values.tolist()

    return dflist
