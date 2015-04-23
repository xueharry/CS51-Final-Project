# Import Python library numpy
import numpy as np

# Training set 1

   # REMEMBER: INCLUDES PREPROCESSING FILE FOR REFERENCE
   def loadMovieLens1(path=os.getcwd()+'/data/ml-100k/u1.base')
   def loadMovieLens1(path=os.getcwd()+'/data/ml-100k/u1.test'):
       
    # Get titles
    movies = {}
    for line in open(path + '/u.item'):
        (id,title) = line.split('|')[0:2]
        movies[id] = title
        
    # Load data
    preferences = {}
    for line in open(path+'/u.data'):
        (user,movieid,rating,ts) = line.split('\t')
        preferences.setdefault(user, {})
        preferences[user][movies[movieid]] = float(rating)
    return preferences
   # END OF PREPROCESSING FILE
   
  movielens_train1 = u1.base
  movielens_test1 = u1.test
  print movielens_train1.shape
  print movielens_test1.shape

   # Save to text file (?) - add to each training set
  movielens_train1.to_csv('../data/movielens_train1.csv')
  movielens_test2.to_csv('../data/movielens_test1.csv')

# Training set 2
movielens_train2 = u2.base
movielens_test2 = u2.test
print movielens_train2.shape
print movielens_test2.shape

# Training set 3
movielens_train3 = u3.base
movielens_test3 = u3.test
print movielens_train3.shape
print movielens_test3.shape

# Training set 4
movielens_train4 = u4.base
movielens_test4 = u4.test
print movielens_train4.shape
print movielens_test4.shape

# Training set 5
movielens_train5 = u5.base
movielens_test5 = u5.test
print movielens_train5.shape
print movielens_test5.shape