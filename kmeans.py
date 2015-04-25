import math
import random
import preprocessing
import sys

class kmeans:
	"Implementation of kmeans algorithm"

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
		# TODO: TEST WHETHER THERE ARE ANY -1 IN LIST
		self.cluster_num = [-1 for i in range(self.num_users)]

		# Initialize with random centroids
		random.seed()
		self.centroids = [[self.data[rand][m] for m in range(self.num_movies)]
							for rand in random.sample(range(self.num_users, self.k))]
		self.assignPointsToCluster()

	def calcCentroid(self, clus):
		"Calculates centroid for a given cluster"
		# Get list of all users in cluster 
		users = [i for i, j in enumerate(self.cluster_num) if j == clus]
		users_list = [self.data[u] for u in users]

		# Calculate centroid by averaging ratings for each of the movies across users
		# in the cluster
		centroid = [sum(i) / len(users_list) for i in zip(*users_list)]

		return centroid

	def updateCentroids(self):
		"Update the centroid of each cluster"
		self.centroids = [self.calcCentroid(c) for c in range(len(self.cluster_num))]

	def assignPointToCluster(self,i):
		"Assign point to cluster"
		minRange = sys.maxsize 
		clusterNum = -1

		# Find closest cluster 
		for centroid in range(self.k):
			d = self.distance(i, centroid)
			if d < minRange:
				minRange = d
				clusterNum = centroid
		# Keep track of number of points changed
		if clusterNum != self.cluster_num(i):
			self.num_points_changed += 1

		# Update sum of square error
		self.sse += min * min

		return clusterNum

	def assignPointsToCluster(self):
	    "Assign each of the points to cluster"
	    self.pointsChanged = 0
	    self.sse = 0
	    self.cluster_num = [self.assignPointToCluster(i)
	    					for i in range(self.num_users)]


	def distance(self, u, c):
		"Distance from user u to centroid c"
		sum_squares = 0.0
		for m in range(self.num_movies):
	           sum_squares += pow(self.data[u][m] - self.centroids[c][m], 2)
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
			if float(self.num_points_changed) / self.num_users < 0.01:
				done = True
			
			# Debugging purposes, check SSE
			print("SSE: %f" % self.sse)

# Run k-means (move this to separate file later)
km = kmeans(preprocessing.load_data(), 1000)
km.kCluster()


