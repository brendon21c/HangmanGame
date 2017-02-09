
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

    play_once()


# This is one full round of the game with as many methods as I could think of.
def play_once():

    guessChance = 0
    playerList = [] # Check list for win conditions.
    gameWord = ChooseRandomWord() ## random word from available list.
    blankSpaces = "_" * len(gameWord)
    wordSplit = list(gameWord) # Split's the word into a list.


    while True:


        print ("Try and guess the " + str(len(gameWord)) + " letter word.")

        print(hamgmanStages[guessChance])
        print("Secret word hint:")
        print(blankSpaces)
        print("Your guesses: \n")
        print (userEntries)
        print("\n")

        userGuess = get_guess()

        check_if_user_guessed(userGuess)

        numCheck = CheckEntry(userGuess, gameWord)

        if numCheck == 0:

            print("Good guess!")
            playerList.append(userGuess)
            blankSpaces = DrawSpaces(userGuess, gameWord, blankSpaces)

        elif numCheck == 1:

            guessChance = guessChance + 1

        if blankSpaces == gameWord:

            print("Congratualations! You win!")
            break

        if guessChance > 6:
            print("Sorry, you lose.")
            break




def check_if_user_guessed(userGuess):

    if userGuess in userEntries:

        print("Sorry, you have guessed that letter.")
        userGuess = input("Try again: ")

    return userGuess

def get_guess():

    userGuess = input("Enter a letter: ")

    return userGuess

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
