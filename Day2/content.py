#data types
#index - subscripting - starts at 0
#-1 starts at end of string so would print o 
print("Hello"[0])

#string
print("123" +"345")

#integer
print(123+345)

#large integers - can use _ instead of , for easy reading
print(123_456_789)

#float
print(3.14)

#boolean
print(True)
print(False)

#check data type
print(type("Hello"))
print(type(123))
print(type(3.14))
print(type(False))

#type conversion/ type casting
print(int("123")+ int("345"))

#print("Number of letters in your name: " + len(input("Enter your name")))
print("Number of letters in your name: " + str(len(input("Enter your name"))))

name_of_user = input("Enter your name")
length_of_name = len(name_of_user)

print(type("Number of letters in your name: ")) #string
print(type(length_of_name)) #int

print("Number of letters in your name: " + str(length_of_name))

#mathematical operators: +,-,*,/,//,**
print(6/3) #implicitly converts to float
print(6//3) #integer - but removes decimal places, doesn't round - floors it
print(2**3) #exponents

#remember PEMDAS - Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
print(3 * 3 + 3 / 3 - 3) #goes left to right with MD, AS - prints 7

#change so it outputs 3
print(3 * (3 + 3) / 3 - 3)

#round function - rounds it instead of floors
#takes 2 inputs, number you want to round and num of digits to round it to
print(round(3.45)) #prints 3
print(round(31.8888, 2)) #print 31.89

#assignment operators: +=, -=, *=, /=
#does the math operator and reassigns to the variable
score = 0
score += 1
print(score)

#f-strings - can use different data types in one string
age = 12
print(f"I am {age} years old.") 