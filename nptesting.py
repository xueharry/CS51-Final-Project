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
        zipped = (a, b)
        if zipped[1] != 0:
        # if b != 0:
        # if b.any != 0:
        # if np.nonzero(b):
        #if 0 in (a,b):
            addition = addition+rmsd_element(zipped[0], zipped[1])
            addition = addition+rmsd_element(a, b)
            i = i+1
        else:
            continue
    if i==0:
        rmsd_inside = 0
    else:
        rmsd_inside = addition/float(i)
    user_rmsd = np.sqrt(rmsd_inside)
    return user_rmsd

def calculate ():
    "Finds the average rmsd for all users"
    km = kmeans(preprocessing.load_data("u.data", 1), 100)
    kmeans_return = km.kCluster()
    user_cluster = kmeans_return[0]
    centroids = kmeans_return[1]

    total_rmsd = 0.0
    test_matrix = preprocessing.testing_load_data("u1.test", 1)
    number_test_users = 0
    for test_user in test_matrix:
        actual = test_matrix[test_user-1]
        predictions = centroids[user_cluster[test_user-1]]
        one_rmsd = one_user_rmsd (predictions, actual)
        total_rmsd = total_rmsd+one_rmsd
        if one_rmsd==0:
            continue
        else:
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
    print "final_evaluation"
    print final_evaluation