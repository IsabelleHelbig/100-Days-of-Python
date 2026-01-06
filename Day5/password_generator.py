import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

#selects amount of characters according to user input
for char in range(0,nr_letters):
    #appends the random choice of letter to the password list
    password.append(random.choice(letters))
    #repeats for as many times as user requests

for char in range(0,nr_symbols):
    password.append(random.choice(symbols))

for char in range(0,nr_numbers):
    password.append(random.choice(numbers))

#prints out password without randomization
print(password)

#randomizing password
# updates existing list without having to reassign
random.shuffle(password)
print(password)

password_string ="".join(password)

#or use
# password_string = ""
# for char in password:
#     password_string += char

print(f"Your password is: {password_string}")

