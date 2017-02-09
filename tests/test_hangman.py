import unittest
from unittest.mock import patch
from Hangman import HangmanGame


#TODO I cannot seem to figure out where to go from here.

class TestHangman(unittest.TestCase):

    @patch('HangmanGame.ChooseRandomWord', return_value = "cat")
    @patch('HangmanGame.get_guess', side_effect = ["c","a","p","t"])
    @patch('HangmanGame.check_if_user_guessed', side_effect = ["c","a","p","t"])
    @patch('HangmanGame.CheckEntry', side_effect = [0, 0, 1, 0]) # 0 is a correct guess, 1 is a fail.
    def test_hangman(self, ):
        pass
