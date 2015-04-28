import math
import random
import nppreprocessing
import sys
import numpy as np

class kmeans:
	"Implementation of kmeans algorithm"

	def __init__(self, matrix, k):
		"Initializer takes in a user-movie matrix and the number of clusters"
                self.data = matrix
                self.k = k
  		self.iteration = 0
  		self.num_points_changed = 0 
  		#self.sse = 0
  		self.num_users = len(self.data)
  		self.num_movies = len(self.data[0]) 
    
  		# List of cluster numbers, all initialized as -1
  		#self.cluster_num = np.array([-1 for i in range(self.num_users)])
  		self.cluster_num = np.random.randint(0, k, size=self.num_users)
    
  		# Initialize with random centroids
  		random.seed()
  		#self.centroids = self.data[np.random.choice(np.arange(self.num_users), self.k, False)]
  		self.centroids = np.zeros((k,self.data.shape[1]))

	def updateCentroids(self):
		"Update the centroid of each cluster"
		#self.centroids = [self.data[self.cluster_num == self.k].mean(axis = 0) for n in range(self.k)]
		#for c in xrange(self.k): 
		#np.mean([self.data[p] for p in xrange(self.k) if self.cluster_num[p] == c], axis=0, out=self.centroids[c])
		for c in xrange(self.k):
	            self.centroids[c] = np.mean([self.data[p] for p in xrange(self.num_users) if self.cluster_num[p]==c], axis=0)

	def assignPointsToCluster(self):
	       "Assign each of the points to cluster"
	       self.old_cluster_num = self.cluster_num
	       self.cluster_num = np.array([np.argmin([np.linalg.norm(p-c) for c in self.centroids]) for p in self.data])
	       
	def kCluster(self):
		"Performs clustering"
		# Flag for whether clustering is done
		done = False

		while not done:
			self.updateCentroids()
			self.assignPointsToCluster()
			self.iteration += 1

			# Check whether clustering is done
			changes = np.sum((self.old_cluster_num - self.cluster_num) != 0)
			if changes == 0:
				done = True
			print("Changes: %d" % changes)

# Run k-means (move this to separate file later)
km = kmeans(nppreprocessing.load_data(), 100)
km.kCluster()


