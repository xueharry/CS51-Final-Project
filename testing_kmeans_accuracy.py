import math
import numpy as np
import pandas as pd
import preprocessing

<<<<<<< HEAD
# Prepare data
base = preprocessing.load_data (path=os.getcwd()+'fake base')
test = preprocessing.load_data (path=os.getcwd()+'fake test')

for l_list in b_list  
    for rating_val in l_list 
        
        

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
=======
class testing:
    "Tests accuracy of kmeans algorithm"
        
    # Get preprocessed data from u.base and u.test
    base = preprocessing.load_data (path=os.getcwd()+'fake base')
        "should be a list of the means from k-mean clustering and each one's ratings"
    test = preprocessing.load_data (path=os.getcwd()+'fake test')
>>>>>>> origin/master

    # Match test_user with his/her row in base matrix (list of rating lists)
        "NOTE: NEED TO CHANGE BASED ON OUTPUT OF RUNNING K-MEANS ALGORITHM- currently assuming looks like [[1;3;5], [2;1;2]...]"
        "method: use index (the user's id) 
    for test_user, test_rating in test
        predicted_ratings = base[test_user]

    # Compare test_user's actual ratings and those predicted by base

        # Test algorithm's prediction against test_user's actual rating for one movie using Root-Mean-Square Deviation formula       
        def rmsd (num1, num2) :
            "where num1 are predictions and num2 are actual"
            return np.sqrt(((num1 - num2) **2).mean())
        
        # Call rmsd formula on all recommended movie ratings returned
        for predicted_ratings_head, predicted_ratings_tail = predicted_ratings[0], predicted_ratings[1:]
            for test_ratings_head, test_ratings_tail = test[0], test[1:]
                sum(rmsd (predicted_ratings_head, test_ratings_head))
                
                "NOTE: THIS PART IS ALL WRONG- need to figure out how to do apply rmsd formula to every prediction/actual movie match"
