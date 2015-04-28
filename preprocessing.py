import os
import math 
import numpy as np
import pandas as pd

def load_data(path=os.getcwd()+'/data/ml-100k/'):

    # Read in file
    rnames = ['user', 'movie', 'rating', 'timestamp']
    df = pd.read_table(path+'u.data', sep='\t', header=None, names=rnames)

    # Matrix of size 1000 x 1700 (rows x cols)
    matrix = [[3 for _ in range(1700)] for _ in range(1000)]

    ### Update the average rating for user, normalize to remove bias 

    # Fill in matrix from data
    for index in df.index: 
        user = df['user'][index] 
        movie = df['movie'][index] 
        rating = df['rating'][index] 
        matrix[user][movie] = rating

    return matrix

