print("welcome to my computer quiz")

playing = input("do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! let's Play :)")
score = 0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print('correct!')
    score += 1
else:
    print("please check your answer. Incorrect answer!")

answer = input("What Does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print('correct!')
    score += 1
else:
    print("please check your answer. Incorrect answer!")

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print('correct!')
    score += 1
else:
    print("please check your answer. Incorrect answer!")

answer = input("What does PSU Stand for? ").lower()
if answer == "power supply unit":
    print('correct!')
    score += 1
else:
    print("please check your answer. Incorrect answer!")
print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) *100) + " % of questions correct!")

