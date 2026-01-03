#conditionals
#if/else
# if condition:
#     do this
# else:
#     do this

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster.")
else:
    print("Sorry you have to grow taller before yyou can ride.")

#comparators >, <, >=, <=, ==, !=
# = is assigning a variable
# == is comparing 

#modulo operator
# gives you the remainder of a division
# 6%2  will be 0
# 6%5 will give 1

#check odd or even
number = int(input("Enter a number:\n"))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

#nesting and Elif
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age < 12:
        print("Please pay $5.")
    elif age <=18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")

#BMI calculator with interpretations
weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
else:
    print("overweight")

#multiple if statements
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want to have a photo taken? Type y for Yes and n for No.")
    if wants_photo == "y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry you have to grow taller before you can ride.")

#logical operators - and, or, not
if age >= 45 and age <= 55:
    # Or
    # 45 <= age <= 55
    print("Everything is going to be ok. Have a free ride on us!")