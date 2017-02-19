# Lab 4
import random

print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down!")
print("Survive your desert trek and out run the natives.")
print()

done = False

milesTraveled = 0
thirst = 0
tiredness = 0
nativeDistance = -20
drinks = 10

while not done:

    nativesUp = random.randrange(7, 15)
    fullSpeed = random.randrange(10, 21)
    moderateSpeed = random.randrange(5, 13)

    print()
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.") 
    print("Q. Quit.")
    print()
    
    userChoice = input("Your choice? ")

    if userChoice.upper() == "Q":
         done = True

    elif userChoice.upper() == "E":
        print("You traveled ", milesTraveled, "miles")
        print("Drinks in canteen: ", drinks)
        print("The natives are", nativeDistance, "miles behind you.")

    elif userChoice.upper() == "D":
        tiredness = 0
        print('The camel is happy and the natives has moved ', nativesUp, "miles")
        
    elif userChoice.upper() == "C":
        milesTraveled = milesTraveled + fullSpeed
        print("You have traveled ", milesTraveled, "miles")  
        thirst = thirst + 1
        tiredness = tiredness + random.randrange(1, 4)
        print("Camel tiredness is ", tiredness)
        nativeDistance = nativeDistance + nativesUp
        print("The natives are getting close by ", nativesUp, "miles")

    elif userChoice.upper() == "B":
        milesTraveled = milesTraveled + moderateSpeed
        print("You have traveled ", milesTraveled, "miles")
        thirst += 1
        tiredness += random.randrange(1, 4)
        nativeDistance = nativeDistance + nativesUp

    elif userChoice.upper() == "A":
        if drinks > 0:
            drinks = drinks - 1
            thirst = 0
            print("You drank from the canteen")
        else:
            print("There are no more drinks")
        
    
    if thirst > 6:
        done = True
        print("You died of thirst!")
        print("Game over!")
    elif thirst >= 4:
        print("You are thirsty!")
        
    if tiredness >= 8:
        done = True
        print("Your camel is dead.")
        print("Game over!")
    elif tiredness >= 5:
        print("Your camel is getting tired!")
         
    if nativeDistance == milesTraveled:
        done = True
        print("The natives caught you!")
        print("Game over!")
        

    if milesTraveled >= 200:
        print("You won!")
        done = True
