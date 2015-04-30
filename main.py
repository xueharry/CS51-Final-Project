import get_recommendations

# Get user's age and check for validity
while True:
    try:
        age = int(raw_input("Please enter your age (between 18 and 65): "))
    except ValueError:
        continue
    if age in range(18, 66):
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

# Get number of movies and check for validity
while True:
    try:
        n = int(raw_input("Please enter number of movie recommendations (between 1 and 20): "))
    except ValueError:
        continue
    if n in range(1, 21):
        break

movies = get_recommendations.top_movies(n,get_recommendations.sim_users_ratings(age, gender.upper(), occupation.lower())) 

print(movies)
