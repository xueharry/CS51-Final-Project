import math
import random
import preprocessing

class kmeans:
	"Implementation of kmeans algorithm"

	def __init__(self, matrix, k):
		"Initializer takes in a user-movie matrix and the number of clusters"

		self.data = matrix
		self.k = k
		#self.counter = 0
		self.iteration = 0
		self.num_points_changed = 0 
		self.sse = 0 

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

		return math.sqrt(sumSquares)

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


