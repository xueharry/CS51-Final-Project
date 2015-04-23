import math
import random
import preprocessing

class kmeans:
	"Implementation of kmeans algorithm"

	def __init__(self, matrix, k):
		"Initializer takes in a user-movie matrix and the number of clusters"

		self.k = k
		#self.counter = 0
		self.iteration = 0
		self.num_points_changed = 0 
		self.sse = 0 

		# List of cluster numbers 
		# TODO: TEST WHETHER THERE ARE ANY -1 IN LIST
		self.cluster_num = [-1 for i in range(len(matrix[0]))]

		# Select random centroids from remaining points
		random.seed()
		self.centroids = TODO 
		
		self.assignPointsToCluster()

	def updateCentroids(self):
		"Determine the centroid of each cluster"

	def assignPointToCluster(self,i):
		"Assign point to cluster"
		# Keep track of changing points
		# Add square of distance to sum of squared error

		return ClusterNum

	def assignPointsToCluster(self):

	def distance(self, i, j):
		"Distance from point i to centroid j"
		sum_squares = sum([pow(i-j),2]):
		for 

		return math.sqrt(sum_squares)

	def kCluster(self):
		"Performs clustering"

		# Flag for whether clustering is done
		done = False

		while not done:
			self.updateCentroids()
			self.assignPointsToCluster()
			self.iterationNumber += 1

			# Check whether clustering is done
			if float(num_points_changed) / self.dats(#total number of points) < 0.01
				done = True
			# Debugging purposes, check SSE


