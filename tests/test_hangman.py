import unittest
from unittest.mock import patch
from Hangman import HangmanGame



class TestHangman(unittest.TestCase):



    def test_get_guess(self):
        pass

    @patch('builtins.input')
    @patch('builtins.print')
    def test_get_guess(self, mock_print, mock_input):

        HangmanGame.userEntries = ['a', 'b', 'c']

        # Test with a valid guess like 'q'

        mock_input.side_effect = 'q'

        return_val = HangmanGame.get_guess()

        self.assertEqual(return_val, 'q')


        # Test with invalid guess

        mock_input.side_effect = ['a', 'b', 'c' , 's']   # invalid, valid

        return_val = HangmanGame.get_guess()

        mock_print.assert_called_with("You already guessed that")


        self.assertEqual(return_val, 's')


    def test_valid_guess(self):

        HangmanGame.userEntries = ['a', 'b', 'c']

        self.assertFalse(HangmanGame.valid_guess('a'))
        self.assertFalse(HangmanGame.valid_guess('b'))
        self.assertTrue(HangmanGame.valid_guess('z'))
        self.assertTrue(HangmanGame.valid_guess('d'))

        self.assertTrue(HangmanGame.valid_guess('D'))
        self.assertFalse(HangmanGame.valid_guess('A'))

        self.assertFalse(HangmanGame.valid_guess('AAAA'))
        self.assertFalse(HangmanGame.valid_guess('123'))


    def test_checkEntry(self):


        self.assertTrue(HangmanGame.checkEntry('a', 'cat'))
        self.assertFalse(HangmanGame.checkEntry('f', 'cat'))

        self.assertFalse(HangmanGame.checkEntry('A', 'cat'))
        self.assertFalse(HangmanGame.checkEntry('123', 'cat'))
        self.assertFalse(HangmanGame.checkEntry('fff', 'cat'))

    # test function to see if blank spaces are replaced with correct letters
    def test_replaceSpacesWithGuessedLetters(self):

        word = 'need'
        spaces = '_' * len(word)

        # letter in word, shold pass.

        return_val = HangmanGame.replaceSpacesWithGuessedLetters('e', word, spaces)

        self.assertEqual(return_val, '_ee_')

        # letter not in word, should pass.

        return_val = HangmanGame.replaceSpacesWithGuessedLetters('f', word, spaces)

        self.assertEqual(return_val, spaces)

    # Testing game win conditions or if it will continue
    def test_update_game_state(self):

        gameWord = 'need'
        userGuess = 'd'
        playerList = ['e','e','n']

        guessChance = 0

        return_val = HangmanGame.update_game_state(playerList, userGuess, gameWord)

        # Should pass
        expected_result_win = "Congratualations! You win!"

        self.assertEqual(return_val, expected_result_win)






if __name__ == '__main__':
    unittest.main()
