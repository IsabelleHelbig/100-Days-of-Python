import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#getting the length of the list to know number of people
number_of_people = len(friends)

#getting the index of the last person on the list 
index_of_last_person = number_of_people - 1

#selecting random person from list index 0 to index of last person in the list
person_selected = random.randint(0, index_of_last_person)

#printing the selected friend with the random index
print(friends[person_selected])




#other way to do this
print(random.choice(friends))