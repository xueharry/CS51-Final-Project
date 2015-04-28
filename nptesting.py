import math
import random
'''import NPTEST_PROCESSING SEPARATE FILE'''
'''import NPKMEANS SEPARATE FILE'''
import sys
import numpy as np

        # Initiate
	def __init__(self, matrix, test_matrix):
		"Initializer takes in a user-movie matrix and the number of clusters"
                self.data = matrix
                self.test_matrix = test_matrix

# Find predictions from test_user's cluster
for x in range(len(self.test_matrix))
    user_cluster = self.cluster_num(test_matrix[x])
    predictions = self.centroids(user_cluster)

# Test results using root-mean-square deviation
x = np.array([1.2,5.0,2.1])
y = np.array([3.4,4.2,1.0])

def rmsd (m1, m2):
      return np.sqrt((((m1.astype(float))-(m2.astype(float)))**2)/2)
      
def clean_up (m1, m2):
      for i, (a, b) in enumerate(zip(m1, m2)):
          if b != 0.0 then rmsd(a,b); i++
          return i

# Calculate!
math = clean_up (matrix, test_matrix)
mean = (math.sum())/i
return mean