import random

# 1
for i in range(10):
    print("Rikke")
print("Done")

# 2
for i in range(20):
    print("Red")
    print("Gold")

# 3
for i in range(2, 101, 2):
    print (i)

# 4
i = 10
while i >= 0:
    print(i)
    i = i - 1

# 5
print("This program takes three numbers and returns the sum.")
total = 0
 
for i in range(3):
    x = int(input("Enter a number: ")) #Input type
    total = total + x #Adds to previous input
print("The total is:", total) #Prints the new total

# 6
my_number = random.randrange(0, 11)
print(my_number)

# 7
my_number = random.random() * 10 + 0
print(my_number)

# 8
print("This program takes seven numbers and returns the sum.")
total = 0
npos  = 0
nzer  = 0
nneg  = 0

for i in range(7):
    user_input = int(input("Enter a number: "))    
    total = total + user_input
    if user_input > 0:
        npos += 1
    elif user_input == 0:
        nzer += 1
    else:
        nneg += 1
        
print("The sum is:", total)
print("Number of positive entities: ", npos)
print("Number of zeros: ", nzer)
print("Number of negative entities: ", nneg)

# 9
heads = 0
tails = 0

for i in range(50):

    randomNumber = random.randrange(0, 2)

    if randomNumber == 0:
        heads += 1
        print("Heads")
    else:
        tails += 1
        print("Tails")

print("Number of heads: ", heads)
print("Number of tails: ", tails)

# 10
print("Choose 1 for Rock, 2 for Paper or 3 for Scissors")

usersChoice = int(input())

randomNumber = random.randrange(1,4)

if randomNumber == 1:
    print("Rock")
elif randomNumber == 2:
    print("Paper")
else:
    print("Scissors")

if randomNumber == 1 and usersChoice == 2:
    print("You win!")
elif randomNumber == 2 and usersChoice == 3:
    print("You win!")
elif randomNumber == 2 and usersChoice == 1:
    print("I win!")
elif randomNumber == 3 and usersChoice == 2:
    print("I win!")
else:
    print("Lets try again!")  

