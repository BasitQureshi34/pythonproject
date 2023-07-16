import random

top_of_range = input("type a Number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0")
        quit()
else:
    print('please type a number next time.')
    quit()

r = random.randint(0 , top_of_range)
guess = 0
while True:
    guess += 1
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('please type a number next time.')
        continue

    if user_guess == r:
        print("Yayyy you got the right answer!")
        break
    elif user_guess > r:
        print("This guess is greater than the actual number!")
    else:
        print("This guess is less than the answer!")

print("You got it in" , guess, "guesses")
