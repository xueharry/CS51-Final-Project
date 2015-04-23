import math 
import numpy as np
import pandas as pd

# Read in data 
rnames = ['user', 'movie', 'rating', 'timestamp']
df = pd.read_table('u.data', sep='\t', header=None,
                        names=rnames)

# Matrix of size 1000 x 1700 (rows x cols)
matrix = [[0 for _ in range(1700)] for _ in range(1000)]

# Fill in matrix from data
for index in df.index: 
    user = df['user'][index] 
    movie = df['movie'][index] 
    rating = df['rating'][index] 
    matrix[user][movie] = rating




