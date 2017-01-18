
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
        blankSpaces = "_" * len(gameWord)
        wordSplit = list(gameWord) # Split's the word into a list.

        print ("Try and guess the " + str(len(gameWord)) + " letter word.")
        print(wordSplit)

        while guessChance <= 6:

            print(hamgmanStages[guessChance])
            print("Secret word hint:")
            print(blankSpaces)
            #print("Secret Word: \n")
            #print(blankSpaces)
            print("Your guesses: \n")
            print (userEntries)
            print("\n")

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
                        blankSpaces = DrawSpaces(userGuess, gameWord, blankSpaces)
                        break

                    elif numCheck == 1:

                        guessChance = guessChance + 1
                        break


            if blankSpaces == gameWord:

                print("Congratualations! You win!")
                break



        if guessChance > 6:
            print("Sorry, you lose.")

        playAgain = input("Do you want to play again? ")

        if playAgain == "y":

            guessChance = 0
            userEntries.clear()
            playerList.clear()

        else:
            print("Thanks for playing")
            playing = False
            break





def ChooseRandomWord():

    wordFile = open("test.txt", "r")

    wordFileList = wordFile.readlines()

    for x,y in enumerate(wordFileList):
        wordFileList[x] = y.replace("\n", "")

    #print(wordFileList)


    randNum = random.randint(0, len(wordFileList) - 1)

    selection = wordFileList[randNum]

    return selection

def CheckEntry(guess, answer):

    if guess in answer:
        userEntries.append(guess)
        return 0

    else:
        print("Sorry, that letter is not in the word.")
        userEntries.append(guess)
        return 1

def DrawSpaces(guess, answer, spaces): # Checks the user answer against word and replaces
                                        # underscores with letters for the hint.
    blankSpaces = list(spaces)

    for x,y in enumerate(blankSpaces):

        if answer[x] == guess:

            blankSpaces[x] = y.replace("_", guess)

    spaceReturn = "".join(blankSpaces)

    return spaceReturn


Main()
