import math
import random
import nppreprocessing
import npkmeans
import sys
import numpy as np


km = npkmeans(nppreprocessing.load_data("u.data"), 100)

predict_array = km.kCluster()
test_array = test_matrix

for i, (a, b) in enumerate(zip(predict_array, test_array)):
      print i, a, b