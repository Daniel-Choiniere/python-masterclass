print("Today is the day I start to learn Python")
print("we can even include 'quotes' inside of strings")
# string concatenation
print("hello" + " world")

# assigning to variables
greeting = "Hello"
# name = input("Please enter your name ")
name = "Dan"
age = 35

# if we want a space we can add that also
print(greeting + ' ' + name)

# checking the type of a variable
print(type(greeting))
print(type(age))

# F-strings
# print(name + "is " + age + " years old") - This will not work because we can not concatanate a int and a string
# With f- Strings we can do it
print(name + f" is {age} years old")
print(type(age))
