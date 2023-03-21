'''
    CISC-121 2022F

    Name: Kashan Rauf
    Student Number: 20369391
    Email: 22kr11@queensu.ca
    Date: 2022-09-26

    I confirm that this assignment solution is my own work and conforms to
    Queen's standards of Academic Integrity
'''

# Open a file for reading
file = open("friendship.txt", "r") # "r"
line = file.readline()

# Reads through file and adds all friendships as pairs
friends=[]
while line != "" :
    l = line.split()
    friends.append(l)
    line = file.readline()
file.close()

# Using a dictionary and reading through 'friends' list, every time a name appears, it adds one friend
dictionary = {}
for person in friends :
    for name in person :
        if (name in dictionary) : 
            dictionary[name]+=1
        else :
            dictionary[name] = 1

# Output for names and number of friends
for person in dictionary :
    print(person, "has", dictionary[person], "friend", end="")
    # Pluralizes output if a person has multiple friends
    if (dictionary[person] > 1) :
        print("s.")
    else :
        print(".")