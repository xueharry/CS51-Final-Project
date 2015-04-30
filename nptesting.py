import math
import random
import preprocessing
import testing_preprocessing
from npkmeans import *
import sys
import numpy as np

# Find predictions from test_user's cluster
def find_centroid (user_id):
    "Gets the user's kmeans cluster by user id and accesses the centroid (with mean ratings for every movie) for predictions"
    km = kmeans(preprocessing.load_data("u.data", 1), 100)
    kmeans_return = km.kCluster()
    user_cluster = kmeans_return[0][user_id-1]
    predict = kmeans_return[1][user_id-1]
    return predict

# Evaluate accuracy of predictions
def rmsd_element (num1, num2):
    "Finds the rmsd between two movie ratings"
     return ((num1.astype(float))-(num2.astype(float)))**2
      
def one_user_rmsd (m1, m2):
    "Finds the average rmsd for all of one user's movie ratings"
    addition = 0.0
    for index, (a, b) in enumerate(zip(m1, m2)):
        if b <> 0:
            addition = addition+rmsd_element(a, b)
            i=i+1
        rmsd_inside = addition/i
        rmsd = np.sqrt(rmsd_inside)
        return rmsd

def calculate ():
    "Finds the average rmsd for all users"
    # kmeans_matrix, test_matrix
    average_rmsd = 0.0
    test_matrix = testing_preprocessing.load_data("u1.test", 1)
    for test_user in test_matrix:
        actual = test_matrix[test_user]
        predictions = find_centroid(test_user)
        average_rmsd = average_rmsd+(one_user_rmsd (predictions, actual))
    final_evaluation = average_rmsd/(len(test_matrix))
    print final_evaluation