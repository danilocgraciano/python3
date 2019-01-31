import hangman
import guessing

def main():

    show_welcome_message()

    show_option_message()

    option = read_option()

    if(option == 1):
        hangman.play()
    elif(option == 2):
        guessing.play()
    else:
        print("Exit")

def show_welcome_message():
    print("#####################################")
    print("#        Choose your game!          #")
    print("#####################################")

def show_option_message():
    print("(1) Hangman (2) Guessing (0) Exit")


def read_option():
    option = 0
    try:
        option = int(input("Which one?"))
        while (option < 0 or option > 2):
            print("Number invalid...")
            show_option_message()
            option = int(input("Which one?"))
    except ValueError:
        print("Please, type a number...")
    else:
        return option
if (__name__ == "__main__"):
    main()
