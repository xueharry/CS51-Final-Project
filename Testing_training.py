class Testing_Training

''' 
 The purpose of this class is to teach the machine to make better 
 predictions while at the same time test that these preditions
 are indeed better than the ones made before 
'''
#The first step is to separate an X amount of data so that testing can be
#More accurate 

#Option one

#Function that would separate N random components of the dataset and return 
#a tuple of the rest of the components and this initial component
def separation (dataset, N):
    '''
    '''

#Option two

'''
One other possibility for testing is to choose subset of individuals who would 
give the most information and run the tests on them. Determining the most 
informative users can be done by implementing the expected information gain 
all users in the dataset and selecting an N amount of users with the 
greater result. The implementation of the following equations should be 
necessary 
''' 
#Function to filter the users and generate a list or dictionary thatcontains 
#the resultinng "expected information gain" 
 def calculate_EIG (dataset):
     '''
     Return type is a dictionary of the users and their EIG 
     '''
 def separate_N_users (dataset, num_of_users) :
     '''Takes in the dictionary created by calculate_EIG, reads the EIGs of the
     users and returns the "num_of_users" with the highest EIGs 
     '''
#This step is optional, the evaluation of the algorithm used to 
#separate the data     
  
def separation_works (dataset):
    
    
#The next step is to check how well the algorithms work
#The results of these functions will be used in the testing class 
#to determine which algorithm is better 

#For each user this function selects a % of the items he/she has rated and
#returns a tuple of X items that will be used for testing and Y items that
#will be used for training 
def separate_Training_testing (data):
    '''
    Input : the list/dictionary of users fiven by separate_N_users
    Output: tuple of the list randomly separated int testing individuals 
    and training individuals
    '''
    
#For testing it is necesary to classify the numerical values of the rankings 
#of the movies into two categories Like, Dislike
def assging_class (dataset) :
    ''' 
    Outputs a dataset of the movies but with either like or 
    dislike assigned instead of a numerical ranking
    '''
def calculate_precision (dataset, dataset2) :
    '''
    this function takes in a dataset completed/ real and the 
    dataset that the classifier returned then it counts the number of liked 
    itemsthat were assigned to the "like class" and the number of items 
    that were assigned to the class. Then it divides the liked items assigned 
    to like over the number of items assigned to the class
    ''' 
    
def calculate_recall (dataset1,dataset2):
    ''' this function behaves similary to the function above except that it
    divides the number of liked items assigned to the class over the total 
    number of liked items 
    ''' 
#This function combines both precision and recall to measure the performance 
#of the algorithm with more accuracy
def optimize (press, recall): 
    ''' Input is the values of precision and recall and output the 
    result of 2*precision*recall/precision+recall
    this value will be passed to testing class to figure the accuracy of the 
    logarithm
    '''