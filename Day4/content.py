#randomization
#computers are deterministic - how to create pseudorandom generators?
#python uses Mersenne Twister as algorithm to randomize

#importing random module to be able to use premade code
import random

#use random module, randint is function in random module using a range from int1 to int2
random_integer = random.randint(1,10)
print(random_integer)

#modules are parts of code that we can call on later to use in different files
#can create new module by making a new file.py and import variables or functions from that file using import
import my_module
print(my_module.my_favourite_number)

#module.function()
#random.random creats floats between 0.0 (inclusive)and 1.0 (not inclusive)
# 0.0 <= random.random() < 1.0
random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

#another way to generating random floats with uniform
#This method may or may not include the upper bound depending on the rounding of the floating point number
# a <= random.uniform(a,b) <= b
random_float = random.uniform(1, 10)
print(random_float)


#lists
#listname = [item1, item2]
fruits = ["Cherry", "Apple", "Pear"]
fruits[0] #cherry
fruits[-1] #pear

#can modify items
fruits[0] = "Orange" # ["Orange", "Apple", "Pear"]

#can add items
fruits.append("Strawberry") # ["Orange", "Apple", "Pear", "Strawberry"]

#can add multiple items 
fruits.extend(["fruit1", "fruit2"])

#list of lists
fruits = ["Cherry", "Apple", "Pear"]
veg = ["Cucumber", "Kale", "Spinnach"]
fruits_and_veg = [fruits, veg]
#The list would look like this: [["Cherry", "Apple", "Pear"], ["Cucumber", "Kale", "Spinnach"]]

fruits_and_veg[0] #["Cherry", "Apple", "Pear"]
fruits_and_veg[0][1] #"Apple"

# index errors
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[49])  # No error
print(states_of_america[50])  # IndexError

# Using len() to find the number of items in a List
num_states = len(states_of_america)
print(states_of_america[num_states - 1])