import os
import sys
import unittest
from unittest.mock import patch, mock_open

# Add the project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.Solution import calculate_sum_of_first_and_last_digits_or_digit_words


class TestCalculateSumOfFirstAndLastDigits(unittest.TestCase):

    def setUp(self):
        """Create a temporary file for testing."""
        self.test_file = "test_input.txt"

    def tearDown(self):
        """Remove the temporary file after tests are done."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    @patch('builtins.open', mock_open(read_data="12\nthree4"))
    def test_valid_file_with_digits_and_words(self):
        """Test with a file containing digits and words."""
        result = calculate_sum_of_first_and_last_digits_or_digit_words(self.test_file)
        self.assertEqual(result, 46)

    @patch('builtins.open', mock_open(read_data="abc\nxyz\nabc\n"))
    def test_valid_file_without_digits(self):
        """Test with a file that does not contain any digits or number words."""
        result = calculate_sum_of_first_and_last_digits_or_digit_words(self.test_file)
        self.assertEqual(result, 0)

    @patch('builtins.open', mock_open(read_data="five6\nseven8"))
    def test_valid_file_with_words_and_digits(self):
        """Test with a file containing number words and digits."""
        result = calculate_sum_of_first_and_last_digits_or_digit_words(self.test_file)
        self.assertEqual(result, 134)

    @patch('builtins.open', mock_open(read_data="one2\ntwo3"))
    def test_valid_file_with_number_words_and_digits(self):
        """Test with a file containing number words and digits."""
        result = calculate_sum_of_first_and_last_digits_or_digit_words(self.test_file)
        self.assertEqual(result, 35)

    def test_file_not_found(self):
        """Test for a file that does not exist."""
        result = calculate_sum_of_first_and_last_digits_or_digit_words("non_existent_file.txt")
        self.assertIsNone(result)

    @patch('builtins.open', mock_open(read_data="abc@#\n1#2$3\n$$\n"))
    def test_file_with_malformed_content(self):
        """Test for a file with content that may cause unexpected behavior."""
        result = calculate_sum_of_first_and_last_digits_or_digit_words(self.test_file)
        self.assertEqual(result, 13)

    @patch('builtins.open', mock_open(read_data=""))
    def test_empty_file(self):
        """Test with an empty file."""
        result = calculate_sum_of_first_and_last_digits_or_digit_words(self.test_file)
        self.assertEqual(result, 0)

    @patch('builtins.open', mock_open(read_data="1x2y\n"))
    def test_single_line_file(self):
        """Test with a file containing just one line with digits."""
        result = calculate_sum_of_first_and_last_digits_or_digit_words(self.test_file)
        self.assertEqual(result, 12)

    @patch('builtins.open', mock_open(read_data="abc1def2\nxyz\n3gh45ij\nno_digits_here\n6kl\n"))
    def test_mixed_content_file(self):
        """Test with a file that has a mix of valid and invalid lines."""
        result = calculate_sum_of_first_and_last_digits_or_digit_words(self.test_file)
        self.assertEqual(result, 113)


if __name__ == "__main__":
    unittest.main()
