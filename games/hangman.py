import random

def play():

    #create_dictionary()

    dictionary = read_dictionary()

    if (dictionary is not None):

        show_welcome_message()

        secret_word = choose_secret_word(dictionary)

        hitted_letters = init_hitted_letters(secret_word)

        hanged = False
        hit = False
        errors = 0

        while(not hanged and not hit):

            kick = read_kick()

            if (kick in secret_word):
                mark_hitted_letters(kick, secret_word, hitted_letters)
            else:
                errors += 1

            hanged = errors == 6
            hit = "_" not in hitted_letters
            print(hitted_letters)

        if (hit):
            show_win_message()
        else:
            show_lost_message(secret_word)

        print("The End")

def create_dictionary():
    file = open("dictionary.txt","w")
    file.write("banana\n")
    file.write("orange\n")
    file.write("pineaple\n")
    file.write("watermelow\n")
    file.write("strawberry\n")
    file.close()

def read_dictionary():
    words = []
    try:
        file = open("dictionary.txt", "r")
        for row in file:
            words.append(row.strip())
        file.close()
    except FileNotFoundError:
        print('Dictionary not found')
    else:
        return words

def show_welcome_message():
    print("#####################################")
    print("#     Welcome to Hangman Game       #")
    print("#####################################")

def choose_secret_word(dictionary):
    random_index = random.randrange(0, len(dictionary))
    return dictionary[random_index].upper()

def init_hitted_letters(secret_word):
    return ["_" for letter in secret_word]

def read_kick():
    return input("Which letter (fruits) ").strip().upper()

def mark_hitted_letters(kick, secret_word, hitted_letters):
    index = 0
    for letter in secret_word:
        if (kick == letter):
            hitted_letters[index] = letter
        index += 1

def show_win_message():
    print("You win :)")

def show_lost_message(secret_word):
    print("You lost :(")
    print("The word was {}".format(secret_word))

if (__name__ == "__main__"):
    play()