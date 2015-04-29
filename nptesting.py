import math
import random
import preprocessing
import testing_preprocessing
from npkmeans import *
import sys
import numpy as np

# Evaluate accuracy of predictions
def rmsd_element (num1, num2):
    "Finds the rmsd between two movie ratings"
    return ((float(num1))-(float(num2)))**2
      
def one_user_rmsd (m1, m2):
    "Finds the average rmsd for all of one user's movie ratings"
    addition = 0.0
    i = 0
    for index, (a, b) in enumerate(zip(m1, m2)):
        if b.any != 0:
            addition = addition+rmsd_element(a, b)
            ++i
    rmsd_inside = addition/float(i)
    rmsd = np.sqrt(rmsd_inside)
    return rmsd

def calculate ():
    "Finds the average rmsd for all users"
    km = kmeans(preprocessing.load_data("u.data", 1), 100)
    kmeans_return = km.kCluster()
    user_cluster = kmeans_return[0]
    centroids = kmeans_return[1]

    average_rmsd = 0.0
    test_matrix = testing_preprocessing.load_data("u1.test", 1)
    number_test_users = 0
    print test_matrix
    for test_user in test_matrix:
        actual = test_matrix[test_user-1]
        predictions = centroids[user_cluster[test_user-1]]
        average_rmsd = average_rmsd+(one_user_rmsd (predictions, actual))
        number_test_users = 1+number_test_users
        "fix this- gives total number of users, not number of users who rated in test file"
    final_evaluation = average_rmsd/float(number_test_users)
    print "actual"
    print actual
    print "predictions"
    print predictions
    print "average_rmsd"
    print average_rmsd
    print "number test users"
    print number_test_users
    print "final_evaluation"
    print final_evaluation