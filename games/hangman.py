def play():
    print("#####################################")
    print("#     Welcome to Hangman Game       #")
    print("#####################################")

    secret_word = "banana"
    hitted_letters = ["_","_","_","_","_","_"]
    hanged = False
    hit = False

    while(not hanged and not hit):
        print(hitted_letters)

        kick = input("Which letter ").strip()

        index = 0
        for letter in secret_word:
            if (kick.upper() == letter.upper()):
                hitted_letters[index] = letter
            index = index + 1


    print("The End")

if (__name__ == "__main__"):
    play()