import hangman
import guessing

print("#####################################")
print("#        Choose your game!          #")
print("#####################################")

print("(1) Hangman (2) Guessing")

game = int(input("Which one?"))

if(game == 1):
    hangman.play()
elif(game == 2):
    guessing.play()
