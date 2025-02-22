import os
import sys
import unittest
from unittest.mock import patch, mock_open

# Add the project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.Solution import extract_and_sum


class TestExtractAndSum(unittest.TestCase):

    def setUp(self):
        """Create a temporary file for testing."""
        self.test_file = "test_input.txt"

    def cleanUp(self):
        """Remove the temporary file after tests are done."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    @patch('builtins.open', mock_open(read_data="abc1def2\n3gh45ij\n6kl\n"))
    def test_valid_file_with_digits(self):
        """Test with a file containing lines with digits."""
        result = extract_and_sum(self.test_file)
        self.assertEqual(result, 113)

    @patch('builtins.open', mock_open(read_data="abc\nxyz\nabc\n"))
    def test_valid_file_without_digits(self):
        """Test with a file that does not contain any digits."""
        result = extract_and_sum(self.test_file)
        self.assertEqual(result, 0)

    def test_file_not_found(self):
        """Test for a file that does not exist."""
        result = extract_and_sum("non_existent_file.txt")
        self.assertIsNone(result)

    @patch('builtins.open', mock_open(read_data="abc@#\n1#2$3\n$$\n"))
    def test_file_with_malformed_content(self):
        """Test for a file with content that may cause unexpected behavior."""
        result = extract_and_sum(self.test_file)
        self.assertEqual(result, 13)

    @patch('builtins.open', mock_open(read_data=""))
    def test_empty_file(self):
        """Test with an empty file."""
        result = extract_and_sum(self.test_file)
        self.assertEqual(result, 0)

    @patch('builtins.open', mock_open(read_data="1x2y\n"))
    def test_single_line_file(self):
        """Test with a file containing just one line with digits."""
        result = extract_and_sum(self.test_file)
        self.assertEqual(result, 12)

    @patch('builtins.open', mock_open(read_data="abc1def2\nxyz\n3gh45ij\nno_digits_here\n6kl\n"))
    def test_mixed_content_file(self):
        """Test with a file that has a mix of valid and invalid lines."""
        result = extract_and_sum(self.test_file)
        self.assertEqual(result, 113)


if __name__ == "__main__":
    unittest.main()
