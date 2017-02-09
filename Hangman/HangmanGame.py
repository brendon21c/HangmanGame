
import random

# I looked up this list on stacksocial, I couldn't think of how to do it.
hangmanStages = ['''
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

userEntries = [] ## Everything the user has guessed already.

guesses_allowed = len(hangmanStages) - 1

guessChance = 0      # The number of guesses the user has made.

gameWord = '' # Blank word to start with, will be replaced with random in game setup.



def main():

    print ("Welcome to Hangman! Guess the word before the unfortunate end.")

    play_once()


# This is one full round of the game with as many methods as I could think of.
def play_once():

    # STEP 1 set up game.
    #guessChance = 0      # The number of guesses the user has made.

    displayHangmanStage(guessChance)

    playerList = [] # A list of letters that the player has guessed that were are in the word.
    gameWord = chooseRandomWord() ## random word from available list.

    # displayWordStatus(gameWord)

    blankSpaces = "_" * len(gameWord)

    # Step two : play game

    while True:

        # Print status update info for user..
        print ("Try and guess the " + str(len(gameWord)) + " letter word.")
        print(gameWord)
        print(guessChance)

        displayHangmanStage(guessChance)

        print("Secret word hint:")
        print(blankSpaces)           # Game logic here - TODO test
        print("Your guesses: \n")
        print (userEntries)           # TODO maybe test this ?
        print("\n")

        # Get user guess (also validation)
        userGuess = get_guess()

        # Report results to user
        # Change score
        # Check if user has won?

        # Where are we with the game state?
        game_result = update_game_state(playerList, userGuess, gameWord)

        # update game word
        blankSpaces = replaceSpacesWithGuessedLetters(userGuess, gameWord, blankSpaces)

        if not game_result == 'game on':
            break

    print(game_result)


def update_game_state(playerList, userGuess, gameWord):

        global guessChance # needed or guessChance cannot be updated.


        guess_in_word = checkEntry(userGuess, gameWord)

        if guess_in_word:
            print("Good guess!")
            playerList.append(userGuess)

        else:
            print("Sorry, that letter is not in the word.")
            guessChance += 1

        game_on = check_if_game_on(playerList, gameWord)

        return game_on


def check_if_game_on(playerList, gameWord):

    if len(playerList) == len(gameWord): # by checking length the game ends as soon as the User guesses right.

        return "Congratualations! You win!"

    if guessChance > guesses_allowed:
        return "Sorry, you lose."

    return "game on"


def valid_guess(userGuess):
    return not userGuess in userEntries


def get_guess():

    userGuess = input("Enter a letter: ")

    while not valid_guess(userGuess,):
        # check_if_user_guessed(userGuess)    # Testing for duplicate guesses
        print("You already guessed that")
        userGuess = input("Enter a letter: ")

    return userGuess


def chooseRandomWord():

    wordFile = open("test.txt", "r")

    wordFileList = wordFile.readlines()

    for x,y in enumerate(wordFileList):
        wordFileList[x] = y.replace("\n", "")

    #print(wordFileList)

    randNum = random.randint(0, len(wordFileList) - 1)

    selection = wordFileList[randNum]

    return selection


def checkEntry(guess, answer):

    ''' Returns True if guess in in word '''

    userEntries.append(guess)

    if guess in answer:
        return True

    else:
        return False


def replaceSpacesWithGuessedLetters(guess, answer, spaces): # Checks the user answer against word and replaces
                                        # underscores with letters for the hint.
    blankSpaces = list(spaces)

    for x,y in enumerate(blankSpaces):

        if answer[x] == guess:

            blankSpaces[x] = y.replace("_", guess)

    spaceReturn = "".join(blankSpaces)

    return spaceReturn


def displayHangmanStage(guessChance):
    print(hangmanStages[guessChance])



if __name__ == '__main__':
    main()
