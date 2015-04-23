class testing 

import math
import numpy as np
import pandas as pd
import preprocessing

# Prepare data
base = preprocessing.load_data (path=os.getcwd()+'fake base')
test = preprocessing.load_data (path=os.getcwd()+'fake test')
'''
MAGALY: HOW TO BREAK UP A LIST
base_head, base_tail = base[0], base[1:]
test_head, test_tail = test[0], test[1:]
Is this a tuple of a user and the list of the ratings?
for the results of the algorithm
eg. 
[(user1, [3,4,5,6,7,8,9,8,7,6,5,4,3), (user2, [3,5,6,4,2,1,5,1,4]) ]
or 
[[2,3,4,6,7,8,9,5,4,3,2,1],
 [4,5,6,7,8,3,5,6,6,3,2,1],
 [3,2,4,5,6,7,2,3,4,5,6,2],] 

Question 2 is test list preprocessed as well?
test file would have some empty stuff 

What can we do to fix it? I am thinking about preprosesing the test part different
because in order to compare it to each of the rankings in the list it must be at the 
same position so if we have the 
base_head = 

# Check which movies test_user has actually watched
for test_user, test_movie, test_rating in test.iteritems() :
test_data = tuple('test_movie', test_rating) for test_user

# Return predicted ratings for test_user's watched/rated movies from running the algorithm on the matrix
for mean_user, mean_movie, mean_rating in RESULT_OF_K_MEANS_ALGORITHM[base].iteritems() :
mean_data = tuple('mean_movie', mean_rating) for mean_user'''
# Match test_user with his/her row in base matrix
for test_user, test_rating in test.iteritems () :
for base_user, base_rating in base.iteritems
return
# Compare test_user's actual ratings and those predicted by base
base[user
# Find predicted ratings for movies test_user has already watched
# Test algorithm's predictions against test_user's actual ratings using Root-Mean-Square Deviation formula
def rmsd (num1, num2) :
sqrt(