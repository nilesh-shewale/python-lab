import unittest
from guess_the_number import process_guess, get_limits, main
from unittest.mock import patch

class TestProcessGuess(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(process_guess(5, 5), 0)
    def test_less_than(self):

        self.assertEqual(process_guess(5, 4), -1)
    def test_greater_than(self):

        self.assertEqual(process_guess(4, 6), 1)

class TestGetLimits(unittest.TestCase):
    @patch('sys.argv', ['guess_the_number.py'])
    def test_missing_arguments(self):
        with self.assertRaises(SystemExit) as err:
            get_limits()
        self.assertEqual(err.exception.code, 1)

    @patch('sys.argv', ['guess_the_number.py', '4'])
    def test_missing_argument(self):
        with self.assertRaises(SystemExit) as err:
            get_limits()
        self.assertEqual(err.exception.code, 1)

    @patch('sys.argv', ['guess_the_number.py', 'one'])
    def test_wrong_argument(self):
        with self.assertRaises(SystemExit) as err:
            get_limits()
        self.assertEqual(err.exception.code, 1)

    @patch('sys.argv', ['guess_the_number.py', 'one', 'two'])
    def test_wrong_arguments(self):
        with self.assertRaises(SystemExit) as err:
            get_limits()
        self.assertEqual(err.exception.code, 1)

    @patch('sys.argv', ['guess_the_number.py', '2', '1'])
    def test_invalid_arguments(self):
        with self.assertRaises(SystemExit) as err:
            get_limits()
        self.assertEqual(err.exception.code, 1)

    @patch('sys.argv', ['guess_the_number.py', '1', '10'])
    def test_valid_arguments(self):
        self.assertEqual(get_limits(), (1, 10))

if __name__ == "__main__":
    unittest.main()