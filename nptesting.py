import math
import random
import preprocessing
import npkmeans
import sys
import numpy as np

# Find predictions from test_user's cluster
def find_centroid (user_id):
    "Gets the user's kmeans cluster by user id and accesses the centroid (with mean ratings for every movie) for predictions"
    km = npkmeans.kmeans(preprocessing.load_data("u.data", 1), 100)
    km.npkmeans.kCluster()
    user_cluster = npkmeans.cluster_num(user_id)
    predictions = npkmeans.centroids(user_cluster)
    return predictions

# Evaluate accuracy of predictions
def rmsd (num1, num2):
    "Finds the rmsd between two movie ratings"
    addition = 0.0
    return np.sqrt((((num1.astype(float))-(num2.astype(float)))**2)/2)
      
def one_user_rmsd (m1, m2):
    "Finds the average rmsd for all of one user's movie ratings"
    for index, (a, b) in enumerate(zip(m1, m2)):
        if b != 0:
            addition = addition+(rmsd(a, b))
            ++i
        return addition/i

def calculate (kmeans_matrix, test_matrix):
    "Finds the average rmsd for all users"
    average_rmsd = 0.0
    for test_user in test_matrix:
        actual = test_matrix[test_user]
        for mean in kmeans_matrix:
            predictions = kmeans_matrix[find_centroid(test_user)]
            average_rmsd = average_rmsd+(one_user_rmsd (predictions, actual))
    final_evaluation = average_rmsd/(len(test_matrix))
    print final_evaluation