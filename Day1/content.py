#Printing
print("Hello World!")

#print practice
print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")

#string manipulation
#\n to add another line
print("Hello world!\nHello world!")
#concactenation
print("Hello" + " " + "Isabelle")

#debug practice
# print(Notes from Day 1")
#  print("The print statement is used to output strings")
# print("Strings are strings of characters"
# priint("String Concatenation is done with the + sign")
# print(("New lines can be created with a \ and the letter n")

print("Notes from Day 1")
print("The print statement is used to output strings")
print("Strings are strings of characters")
print("String Concatenation is done with the + sign")
print("New lines can be created with a \ and the letter n")

#inputs
#input is run before the print statement
print("Hello" + " " + input("What is your name?") + "!")

#variables
#name = "whatever"
#name_with_underscores_and_lowercase
print(len(input("What is your name?")))

username = input("What is your name?")
length = len(username)
print(length)

#variables practices
#We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains juice. Write 3 lines of code to switch the contents of the variables. You are not allowed to type the words "milk" or "juice". You are only allowed to use variables to solve this exercise.
glass1 = "milk"
glass2 = "juice"

temp=glass1
glass1=glass2
glass2=temp

print(glass1)
print(glass2)

