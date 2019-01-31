import random

def play():

    secret_number = random.randrange(1, 101)
    score = 1000
    level = 0

    show_welcome_message()

    show_level_message()

    while(level == 0):
        level = read_level()

    attempts = calculate_attempts(level)

    for round in range(1, attempts + 1):

        try:
            print("Attempt {0} from {1}".format(round, attempts))

            kick = 0
            while(kick == 0):
                kick = read_kick()

            hit = kick == secret_number

            if (hit):
                print("Congratulations, you WIN, and your score is {}!".format(score))
                break
            else:
                show_feedback_message(kick, secret_number)
                score = score - calculate_lost_score(kick, secret_number)

        except ValueError:
            print("Please, type a number...")

    print("The End")

def show_welcome_message():
    print("#####################################")
    print("#     Welcome to Guessing Game      #")
    print("#####################################")

def show_level_message():
    print("(1) Easy, (2) Medium, (3) Hard")

def read_level():
    try:
        level = int(input("Choose the level: "))
        while (level < 1 or level > 3):
            print("Number invalid...")
            show_level_message()
            level = int(input("Choose the level: "))
    except ValueError:
        print("Please, type a number...")
        return 0
    else:
        return level

def calculate_attempts(level):
    if (level == 1):
        attempts = 20
    elif(level == 2):
        attempts = 10
    else:
        attempts = 5
    return attempts

def read_kick():
    try:
        kick = int(input("Type a number between 1 an 100: "))
        while (kick < 1 or kick > 100):
            print("Number invalid...")
            kick = int(input("Type a number between 1 an 100: "))
        return kick
    except ValueError:
        print("Please, type a number...")
        return 0

def show_feedback_message(kick, secret_number):
    print("You missed!")

    greater_than = kick < secret_number
    less_than = not greater_than

    if (greater_than):
        print("The number is bigger!")
    elif (less_than):
        print("The number is smaller!")

def calculate_lost_score(kick, secret_number):
    return abs((secret_number - kick))

if (__name__ == "__main__"):
    play()
