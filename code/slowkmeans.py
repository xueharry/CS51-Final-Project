# Our initial implementation of kmeans, which took an hour to run.
# Do not use this in grading.
# Version actually used in final implementation can be found in npkmeans.py

import math
import random
import preprocessing
import sys

class kmeans:
	"Implementation of kmeans algorithm (NOT USED IN ACTUAL IMPLEMENTATION)"

	def __init__(self, matrix, k):
		"Initializer takes in a user-movie matrix and the number of clusters"
		self.data = matrix
		self.k = k
		self.iteration = 0
		self.num_points_changed = 0 
		self.sse = 0
		self.num_users = len(self.data)
		self.num_movies = len(self.data[0]) 

		# List of cluster numbers, all initialized as -1
		self.cluster_num = [-1 for i in range(self.num_users)]

		# Initialize with random centroids
		random.seed()
		self.centroids = [[self.data[rand][m] for m in range(self.num_movies)]
			for rand in random.sample(range(self.num_users), self.k)]
		self.assignPointsToCluster()

	def calcCentroid(self, clus):
		"Calculates centroid for a given cluster"
		# Get list of all users in cluster
		# Returns [0,3,4,...] the indices of users who are in cluster clus 
		users = [i for i, j in enumerate(self.cluster_num) if j == clus]
		if len(users) == 0:
			centroid = [self.data[random.randint(0,self.num_users-1)][m] for m in range(self.num_movies)]
		else:
			# Returns [self.data[0],self.data[3]...] list of lists of movies for above users
			users_list = [self.data[u] for u in users]
			# Calculate centroid by averaging ratings for each of the movies across users in the cluster
			centroid = [float(sum(i)) / float(len(users_list)) for i in zip(*users_list)]

		# Returns list of average ratings for each movie across cluster
		return centroid

	def updateCentroids(self):
		"Update the centroid of each cluster"
		self.centroids = [self.calcCentroid(c) for c in range(self.k)]
            
	def assignPointToCluster(self,i):
		"Assign point to cluster"
		minRange = float(sys.maxsize) 
		clusterNum = -1

		# Find closest cluster 
		for centroid in range(self.k):
			d = self.distance(i, centroid)
			if d < minRange:
				minRange = d
				clusterNum = centroid
		# Keep track of number of points changed
		if clusterNum != self.cluster_num[i]:
			self.num_points_changed += 1
		# Update sum of square error
		self.sse += minRange * minRange 

		return clusterNum

	def assignPointsToCluster(self):
		"Assign each of the points to cluster"
		self.num_points_changed = 0
		self.sse = 0
		self.cluster_num = [self.assignPointToCluster(i)
			for i in range(self.num_users)]

	def distance(self, u, c):
		"Distance from user u to centroid c"
		sum_squares = 0.0
		for m in range(self.num_movies):
			sum_squares += pow(self.data[u][m] - self.centroids[c][m],2)
		return math.sqrt(sum_squares)

	def kCluster(self):
		"Performs clustering"

		# Flag for whether clustering is done
		done = False

		while not done:
			self.updateCentroids()
			self.assignPointsToCluster()
			self.iteration += 1

			# Check whether clustering is done
			if float(self.num_points_changed) / float(self.num_users) < 0.01:
				done = True
			print(self.cluster_num)

		# SSE for debugging purposes
		print("SSE: %f" % self.sse)


