import math
import numpy as np
import pandas as pd
import preprocessing

class testing:
    "Tests accuracy of kmeans algorithm"
        
    # Get preprocessed data from u.base and u.test
    base = preprocessing.load_data (path=os.getcwd()+'fake base')
        "should be a list of the means from k-mean clustering and each one's ratings"
    test = preprocessing.load_data (path=os.getcwd()+'fake test')

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