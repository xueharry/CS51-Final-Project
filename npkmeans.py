import preprocessing
import numpy as np

class kmeans:
	"Implementation of kmeans algorithm"

	def __init__(self, matrix, k):
		"Initializer takes in a user-movie matrix and the number of clusters"
                self.data = matrix
                self.k = k
  		self.iteration = 0
  		self.num_users = len(self.data)
  		self.num_movies = len(self.data[0]) 
    
  		# List of cluster numbers, initalized randomly 
  		self.cluster_num = np.random.randint(0, k, size=self.num_users)
    
  		# Initialize centroids to zero
  		self.centroids = np.zeros((k,self.data.shape[1]))

	def updateCentroids(self):
		"Update the centroid of each cluster"
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
		print self.cluster_num

# Run k-means (move this to separate file later)
km = kmeans(preprocessing.load_data("u.data", 1), 100)
km.kCluster()


