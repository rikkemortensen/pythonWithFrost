print("ARE YOU READY FOR SOME UX FUN?") # Question printed first

print()

score = 0

print("1. What does UX stand for?")
answer = input()
if answer.lower() == "user experience": 
    print("Correct!")
    score += 1
else:
    print("Incorrect! It is User Experience.")

print()

print("2. Is design and UX the same?")
answer = input()
if answer.lower() == "no": 
    print("Correct!")
    score += 1
else:
    print("Incorrect! User Experience is much more!")

print()

print("3. Which of these is not a qualitative method?")
print("A. Observations")
print("B. Interviews")
print("C. Questionnair")
user_input = input()
if user_input.upper() == "C":
    print("Correct!")
    score += 1
else:
    print("Incorrect, it is questionnairs.")

print()

print("4. What is the most important skill, when doing research in your field?")
answer = input()
if answer.lower() == "empathy": 
    print("Correct!")
    score += 1
else:
    print("Come on bro, u gotta have empathy man!")

print()

print("5. What is the recommended method for interviewing kids?")
answer = input()
if answer.lower() == "word cards": 
    print("Correct!")
    score += 1
else:
    print("No, word cards are very effective!")

print()

print("6. What is the first step in the Iterative Design Process?")
answer = input()
if answer.lower() == "research": 
    print("Correct!")
    score += 1
else:
    print("No, you gotta do your research first! How do you else know what to create?")

print("Congratulations, you got", score, "right")
print("That is  a score of", score/6*100, "percent")

# BLRUP BLURP

