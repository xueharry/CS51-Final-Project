# Get user's age and check for validity
while True:
    try:
        age = int(input("Please enter your age: "))
    except ValueError:
        print("Please print a valid age!: ")
        continue
    if age <= 0 or age > 100:
    	print("Please enter a valid age!: ")
    else:
        break

# Get user's gender and check for validity
while True:
	try:
		gender = input("Please enter your gender (M/F): ")

# Get user's occupation and check for validity
while True:
	try:
		occupation = input("Please enter your occupation: (administrator artist doctor educator engineer entertainment executive healthcare homemaker lawyer librarian marketing none other programmer retired salesman scientist student technician writer: ")
