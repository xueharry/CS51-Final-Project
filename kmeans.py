import math
import random
import preprocessing

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
		self.centroids = [[self.data[i][rand] for i in range(1, num_users)]
							for rand in random.sample(range(num_movies, self.k)]
		self.assignPointsToCluster()

	def updateCentroids(self):
		"Determine the centroid of each cluster"
		num_members = [self.cluster_num.count(i) for i in range(len(self.centroids))]
		self.centroids = [[sum([self.data[k][i]
								for i in range(num_movies)
								if self.cluster_num[i] == centroid])/members[centroid]
							for k in range(1, len(self.data))]
						for centroid in range(len(self.centroids))]

	def assignPointToCluster(self,i):
		"Assign point to cluster"
		minRange = sys.maxsize 
		clusterNum = -1

		# Find closest cluster
		if centroid in range(self.k):
			d = self.distance(i, centroid)
			if d < minRange:
				min = clusterNum = centroid
		# Keep track of number of points changed
		if clusterNum != self.cluster_num(i)
			self.num_points_changed += 1

		# Update sum of square error
		self.sse += min * min

		return clusterNum

	def assignPointsToCluster(self):
	    "Assign each of the points to cluster"
	    self.pointsChanged = 0
	    self.sse = 0
	    self.cluster_num = [self.assignPointToCluster(i)
	    					for i in range(num_users)]


	def distance(self, i, c):
		"Distance from point i to centroid c"
		for n in range (1,len(matrix[0])):
			sum_squares += [pow(matrix[n][i]-self.centroid[c][n-1]),2]
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


