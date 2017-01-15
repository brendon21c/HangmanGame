
import random

# I looked up this list on stacksocial, I couldn't think of how to do it.
hamgmanStages = ['''
    +---+
    |   |
        |
        |
        |
        |
===========
    ''', '''
    +---+
    |   |
    O   |
        |
        |
        |
=========== ''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
=========== ''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
=========== ''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
=========== ''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
=========== ''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
=========== '''

]

userEntries = [] ## List to catalog the user's entries.



def Main():

    print ("Welcome to Hangman! Guess the word before the unfortunate end.")

    guessChance = 0
    playerList = [] # Check list for win conditions.


    while True:

        gameWord = ChooseRandomWord() ## random word from available list.

        wordSplit = list(gameWord) # Split's the word into a list.

        print ("Try and guess the " + str(len(gameWord)) + " letter word.")

        while guessChance <= 6:

            print(hamgmanStages[guessChance])
            print (userEntries)

            userGuess = input("Enter a letter: ")

            while True:

                if userGuess in userEntries:

                    print("Sorry, you have guessed that letter.")
                    userGuess = input("Try again: ")

                else:

                    numCheck = CheckEntry(userGuess, gameWord)

                    if numCheck == 0:

                        print("Good guess!")
                        playerList.append(userGuess)
                        break

                    elif numCheck == 1:

                        guessChance = guessChance + 1
                        break

            if len(playerList) == len(wordSplit):

                print("Congratualations! You win!")
                break


        playAgain = input("Do you want to play again? ")

        if playAgain.lower is "y":

            guessChance = 0
            userEntries.clear
            playerList.clear


        else:
            print("Thanks for playing")
            playing = False
            




def ChooseRandomWord():

    wordList = ["cat","dog","bird","Superman","foster","culinary","onitama",
    "dictionary","python","matter","energy","collider","baseball","formula",
    "ticket","kyptonite","sanguine","byron","fitzgerald","alhambra"
    ]

    randNum = random.randint(0, len(wordList) - 1)

    selection = wordList[randNum]

    return selection

def CheckEntry(guess, answer):

    if guess in answer:
        userEntries.append(guess)
        return 0

    else:
        print("Sorry, that letter is not in the word.")
        userEntries.append(guess)
        return 1



Main()
