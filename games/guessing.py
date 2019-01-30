import random

def play():

    secret_number = random.randrange(1, 101)
    score = 1000
    level = 0

    showWelcomeMessage()

    showLevelMessage()

    while(level == 0):
        level = readLevel()

    attempts = getAttempts(level)

    for round in range(1, attempts + 1):

        try:
            print("Attempt {0} from {1}".format(round, attempts))

            kick = 0;
            while(kick == 0):
                kick = readKick()

            hit = kick == secret_number

            if (hit):
                print("Congratulations, you WIN, and your score is {}!".format(score))
                break
            else:
                showFeedbackMessage(kick, secret_number)
                score = score - calculateLostScore(kick, secret_number)

        except ValueError:
            print("Please, type a number...")

    print("The End")

def showWelcomeMessage():
    print("#####################################")
    print("#   Welcome to Guessing Game Game   #")
    print("#####################################")

def showLevelMessage():
    print("(1) Easy, (2) Medium, (3) Hard")

def readLevel():
    try:
        level = int(input("Choose the level:"))
        while (level < 1 or level > 3):
            print("Number invalid...")
            showLevelMessage()
            level = int(input("Choose the level:"))
        return level

    except ValueError:
        print("Please, type a number...")
        return 0;

def getAttempts(level):
    if (level == 1):
        attempts = 20
    elif(level == 2):
        attempts = 10
    else:
        attempts = 5
    return attempts

def readKick():
    try:
        kick = int(input("Type a number between 1 an 100:"))
        while (kick < 1 or kick > 100):
            print("Number invalid...")
            kick = int(input("Type a number between 1 an 100:"))
        return kick
    except ValueError:
        print("Please, type a number...")
        return 0;

def showFeedbackMessage(kick, secret_number):
    print("You missed!")

    greater_than = kick < secret_number
    less_than = not greater_than

    if (greater_than):
        print("The number is bigger!")
    elif (less_than):
        print("The number is smaller!")

def calculateLostScore(kick, secret_number):
    return abs((secret_number - kick))

if (__name__ == "__main__"):
    play()