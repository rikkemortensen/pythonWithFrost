# 1

temperature = float(input("Temperature: ")) # Parenthesis in the end
if temperature > 90:
    print("It is hot outside.")
else:
    print("It is not hot out.")

# 2

number = float(input("Type a number: "))
if number > 0:
    print("This number is positive")
elif number < 0:
    print("This number is negative")
else:
    print("This number is 0")

# 3

num = int(input("Type a number: "))
if num > -10 and num <= 10:
    print("Success")
else:
    print("No success")

# 4

print("A cherry is a: ")
print("A. Dessert topping")
print("B. Desert topping")
user_input = input()
if user_input.upper() == "A":
    print("Correct!")
else:
    print("Incorrect.")

# 5

x = 4
if x > 0:
    print("x is positive.")
elif x < 0:
    print("x is not positive.")
else:
    print("x is 0.")

# 6

x = int(input("Enter a number: ")) #State that input is a int
if x == 3: # x is equal to 3 and the ":"
    print("You entered 3")
else:
    print("You did not enter 3") # Adding a condition for enterring 
# other numbers than 3.

# 7

print("What is the name of Dr. Bunsen Honeydew's assistant?") # Question printed first
answer = input() # Users input
if answer.lower() == "beaker": # Always converting input to lower case. Edit variable name. Added "=". 
    print("Correct!")
else: # ":" added
    print("Incorrect! It is Beaker.")


# 8

print("How are you today?")
x = input()
if x.lower() == "happy" or x.lower() == "glad":
    print("That is good to hear!")
else:
    print("Go be awesome!")

# 9

x = 5
y = x == 6
z = x == 5
print("x=", x)
print("y=", y)
print("z=", z)
if y:
    print("Fizz")
if z:
    print("Buzz")

# What I think it prints:
# x=5
# y=False
# z=True
# Buzz

# Okay, I was missing some spaces. Prints Buzz, because y is false, so it prints the true z.

# 10

x = 5
y = 10
z = 10
print(x < y)
print(y < z)
print(x == 5)
print(not x == 5)
print(x != 5)
print(not x != 5)
print(x == "5")
print(5 == x + 0.00000000001)
print(x == 5 and y == 10)
print(x == 5 and y == 5)
print(x == 5 or y == 5)

# What I think it prints:
# True
# False
# True
# False
# False
# False # I didn't see the 'not'.
# False
# False
# True
# False
# True

# 11

print("3" == "3")
print(" 3" == "3")
print(3 < 4)
print(3 < 10)
print("3" < "4")
print("3" < "10")
print( (2 == 2) == "True" )
print( (2 == 2) == True )
print(3 < "3")

# What I think it prints:
# True
# False
# True
# True
# True
# True # I was not correst here
# False
# True
# False # This can not run

# 12

print("Welcome to Oregon Trail!")
 
print("A. Banker")
print("B. Carpenter")
print("C. Farmer")
 
user_input = input("What is your occupation? ")
 
if user_input.upper() == "A":
    money = 100
elif user_input.upper() == "B":
    money = 70
elif user_input.upper() == "C":
    money = 50
 
print("Great! you will start the game with", money, "dollars.")



