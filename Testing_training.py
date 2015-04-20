class Testing_Training

''' 
 The purpose of this class is to teach the machine to make better 
 predictions while at the same time test that these preditions
 are indeed better than the ones made before 
'''

#Function that would separate one of the components of the dataset and return 
#a tuple of the rest of the components and this initial component
def separation (dataset):
    '''
    '''

#Function to test 


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