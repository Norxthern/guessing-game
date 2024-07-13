import random
print("Welcome to guessing game!")
while True:
    try:
        ask = int(input("Choose one from the following: \n1. Singleplayer\n2. Against AI\n"))
        if ask == 1 or ask == 2:
            break
    except ValueError:
        print("Numbers only! Choose 1 or 2.")




def singleplayer():
    num = int(input("Enter a number (minimum).\n"))
    num3 = int(input("Enter another number (maximum).\n"))
    number = random.randint(num, num3)
    tries = int(input("Tries: "))
    print(f"Random number generated in range {num}-{num3}.")
    while True:
       
        guess = int(input("Try and guess a number! "))
        if guess == number:
            print("Congratulations! You guessed correct with " + str(tries) + " tries left!")
            break

        if guess < number:
            tries -= 1
            print("Your guess is smaller than the number! " + str(tries) + " tries left.")
           
        if guess > number:
            tries -= 1
            print("Your guess is bigger than the number! " + str(tries) + " tries left.")
        if tries == 0:
            print("You have 0 tries left! Game over. The number was " + str(number) + ".")
            break
       


def easyai():
    number = random.randint(0, 80)
    tries = 3
    print("Random number generated!")
    print("Range is from 0 to 80. You have " + str(tries) + " tries.")
    while True:
       
        guess = int(input("Try and guess a number! "))
        if guess == number:
            print("Congratulations! You guessed correct with " + str(tries) + " tries left!")
            break

        if guess < number:
            tries -= 1
            print("Your guess is smaller than the number! " + str(tries) + " tries left.")
           
        if guess > number:
            tries -= 1
            print("Your guess is bigger than the number! " + str(tries) + " tries left.")
        if tries == 0:
            print("You have 0 tries left! Game over. The number was " + str(number) + ".")
            break

def medai():
    number = random.randint(0, 400)
    tries = 5
    print("Random number generated!")
    print("Range is from 0 to 400. You have " + str(tries) + " tries.")
    while True:
        guess = int(input("Try and guess a number! "))
        if guess == number:
            print("Congratulations! You guessed correct with " + str(tries) + " tries left!")
            break

        if guess < number:
            tries -= 1
            print("Your guess is smaller than the number! " + str(tries) + " tries left.")
           
        if guess > number:
            tries -= 1
            print("Your guess is bigger than the number! " + str(tries) + " tries left.")
        if tries == 0:
            print("You have 0 tries left! Game over. The number was " + str(number) + ".")
            break

def hardai():
    number = random.randint(0, 700)
    tries = 6
    print("Random number generated!")
    print("Range is from 0 to 700. You have " + str(tries) + " tries.")
    while True:
        guess = int(input("Try and guess a number! "))
        if guess == number:
            print("Congratulations! You guessed correct with " + str(tries) + " tries left!")
            break

        if guess < number:
            tries -= 1
            print("Your guess is smaller than the number! " + str(tries) + " tries left.")
           
        if guess > number:
            tries -= 1
            print("Your guess is bigger than the number! " + str(tries) + " tries left.")
        if tries == 0:
            print("You have 0 tries left! Game over. The number was " + str(number) + ".")
            break



def exhardai():
    number = random.randint(0, 5000)
    tries = 15
    print("Random number generated!")
    print("Range is from 0 to 1,500. You have " + str(tries) + " tries.")

    while True:
       
        guess = int(input("Try and guess a number! "))

        if guess == number:
            print("Congratulations! You guessed correct with " + str(tries) + " tries left!")
            break

        if guess < number:
            tries -= 1
            print("Your guess is smaller than the number! " + str(tries) + " tries left.")
           
        if guess > number:
            tries -= 1
            print("Your guess is bigger than the number! " + str(tries) + " tries left.")
        if tries == 0:
            print("You have 0 tries left! Game over. The number was " + str(number) + ".")
            break


def imp():
    number = random.randint(0, 15000)
    tries = 20
    print("Random number generated!")
    print("Range is from 0 to 15000. You have " + str(tries) + " tries.")
    while True:
       
        guess = int(input("Try and guess a number! "))

        if guess == number:
            print("Congratulations! You guessed correct with " + str(tries) + " tries left!")
            break

        if guess < number:
            tries -= 1
            print("Your guess is smaller than the number! " + str(tries) + " tries left.")
           
        if guess > number:
            tries -= 1
            print("Your guess is bigger than the number! " + str(tries) + " tries left.")
        if tries == 0:
            print("You have 0 tries left! Game over. The number was " + str(number) + ".")
            break

if ask == 1:
    singleplayer()
elif ask == 2:
    difficulty = int(input("Diffuclty:\n1. Easy\n2. Medium\n3. Hard\n4. Extremely Hard\n5. Impossible\n"))
    if difficulty == 1:
        easyai()
    elif difficulty == 2:
        medai()
    elif difficulty == 3:
        hardai()
    elif difficulty == 4:
        exhardai()
    elif difficulty == 5:
        imp()