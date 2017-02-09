import unittest
from unittest.mock import patch
from Hangman import HangmanGame


#TODO I cannot seem to figure out where to go from here.

class TestHangman(unittest.TestCase):

    # @patch('HangmanGame.ChooseRandomWord', return_value = "cat")
    # @patch('HangmanGame.get_guess', side_effect = ["c","a","p","t"])
    # @patch('HangmanGame.check_if_user_guessed', side_effect = ["c","a","p","t"])
    # @patch('HangmanGame.CheckEntry', side_effect = [0, 0, 1, 0]) # 0 is a correct guess, 1 is a fail.
    # def test_hangman(self, ):
    #     pass


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







        # HangmanGame.check_if_user_guessed('a')






if __name__ == '__main__':
    unittest.main()
