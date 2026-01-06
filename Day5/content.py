#Loops

#For Loop
#for item in list_of_item:
    #do something to each item

# for <variable name of each item> in <a List>:
#     <do something>
#     <do something else> 

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
    # apple, apple pie, peach, peach pie....
    print(fruits) #Apple, Apple pie, ['Apple', 'Peach', 'Pear'], Peach, Peach pie, ['Apple', 'Peach', 'Pear']

#sum
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(sum(student_scores))

#sum looks like this in the background
sum = 0
for score in student_scores:
    sum += score
    
print(sum)

#max
print(max(student_scores))

#max function manually
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)

#for loops with range function
# a <= range(a, b) < b
for number in range(1, 10):
    print(number) #prints out 1-9 

# 3 is the step amount, so from 1 to 11 it will step up 3 every time
for number in range(1, 11, 3):
    print(number) #prints out 1,4,7,10

#gauss challenge - add up all the numbers from 1-100
sum = 0
for number in range(1,101):
    sum += number

print(sum)