import get_recommendations

# Get user's age and check for validity
while True:
    try:
        age = int(raw_input("Please enter your age (between 18 and 65): "))
    except ValueError:
        continue
    if age in (18, 65):
        break

# Get user's gender and check for validity
while True:
    try:
        gender = str(raw_input("Please enter your gender (M or F): "))
    except ValueError:
        continue
    if gender.upper() in ('M', 'F'):
        break

# Get user's occupation and check for validity
while True:
    try:
        occupation = str(raw_input("Please enter your occupation (administrator artist doctor educator engineer entertainment executive healthcare homemaker lawyer librarian marketing none other programmer retired salesman scientist student technician writer): "))
    except ValueError:
        continue
    if occupation.lower() in ('administrator', 'artist', 'doctor', 'educator', 'engineer', 'entertainment', 'executive', 'healthcare', 'homemaker', 'lawyer', 'librarian', 'marketing', 'none', 'other', 'programmer', 'retired', 'salesman', 'scientist', 'student', 'technician', 'writer'):
        break 

m = get_recommendations.top_movies(get_recommendations.average_ratings(get_recommendations.get_sim_users_centroids(get_recommendations.get_sim_users(age, gender.upper(), occupation.lower()))))
print(m)

#get_recommendations.get_top_ten(age, gender.upper(), occupation.lower())



#Given a list of movie ratings
#Find indexes of top ten
#Return titles