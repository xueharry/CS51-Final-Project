import math
import random
import preprocessing
from npkmeans import *
import sys
import numpy as np

# Evaluate accuracy of predictions
def rmsd_element (num1, num2):
    "Finds the inside of rmsd formula between two movie ratings"
    return ((float(num1))-(float(num2)))**2
      
def one_user_rmsd (m1, m2):
    "Finds the average rmsd for all of one user's movie ratings"
    addition = 0.0
    i = 0
    for index, (a, b) in enumerate(zip(m1, m2)):
        if b <> 0:
        # if zipped[1] != 0:
        # if b != 0:
        # if b.any != 0:
        # if np.nonzero(b):
        #if 0 in (a,b):
            # addition = addition+rmsd_element(zipped[0], zipped[1])
            addition = addition+rmsd_element(a, b)
            i = i+1
            print "index"
            print index
            print "b is not 0"
            print "addition"
            print addition
        else:
            print "b is 0"
            print "addition"
            print addition
            continue
    if i==0:
        rmsd_inside = 0
    else:
        rmsd_inside = addition/float(i)
    user_rmsd = np.sqrt(rmsd_inside)
    return user_rmsd

def calculate ():
    "Finds the average rmsd for all users"
    test_matrix = [[5,0,0,0,4],[0,0,0,0,0], [1,2,3,4,5]]
    predict_matrix = [[3,4,5,4,3], [3,4,3,2,1], [1,1,1,1,1]]

    total_rmsd = 0.0
    number_test_users = 0
    user_id = 0
    for test_user in test_matrix:
        actual = test_user
        predictions = predict_matrix[user_id]
        one_rmsd = one_user_rmsd (predictions, actual)
        total_rmsd = total_rmsd+one_rmsd
        user_id = user_id + 1
        if one_rmsd==0:
            print "one_rmsd = 0"
            continue
        else:
            print "one_rmsd is not 0"
            number_test_users = number_test_users+1
            "attempted to fix users to be number of users in test file, not number of users in array (which is all of them)"
    final_evaluation = total_rmsd/float(number_test_users)
    print "actual"
    print actual
    print "predictions"
    print predictions
    print "total_rmsd"
    print total_rmsd
    print "number test users"
    print number_test_users
    print "user_id"
    print user_id
    print "final_evaluation"
    print final_evaluation