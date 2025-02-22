import logging
import os
import re

# Configure logging to capture errors and other log messages
logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")


def calculate_sum_of_first_and_last_digits_or_digit_words(file_path: str) -> int:
    """
    Calculate the sum of the first and last digits (or digit words) found in each line of a file.

    Args:
    - file_path (str): The path to the input file containing lines with digits and number words.

    Returns:
    - int: The total sum of first and last digits across all lines in the file.
    - None: If an error occurs (e.g., file not found or I/O error).
    """
    # List of number words corresponding to digits 1 through 9
    number_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    total_sum = 0

    # Create a regex pattern for matching number words and digits
    pattern = "(?=(" + "|".join(number_words) + "|\\d))"

    try:
        # Open the file and process each line
        with open(file_path, "r") as file:
            for line in file:
                digits = []
                matches = re.findall(pattern, line)

                # Map the matched words to their corresponding digits
                for match in matches:
                    if match in number_words:
                        digits.append(str(number_words.index(match) + 1))
                    elif match.isdigit():
                        digits.append(match)

                # Check if we found digits and calculate the sum of the first and last
                if digits:
                    total_sum += int(digits[0] + digits[-1])

    except FileNotFoundError:
        logging.error(f"File '{file_path}' not found.")
        return None
    except IOError as io_error:
        logging.error(f"IO error occurred while accessing the file '{file_path}': {io_error}")
        return None
    except Exception as ex:
        logging.exception(f"An unexpected error occurred: {ex}")
        return None

    return total_sum


def main():
    """
    Main function to get the file name and run the calculation and display the result.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = input("Enter the name of the file to read (from 'resources' folder): ")
    file_path = os.path.join(script_dir, '..', 'resources', file_name)
    result = calculate_sum_of_first_and_last_digits_or_digit_words(file_path)

    if result is not None:
        print(f"Total sum: {result}")
    else:
        print("An error occurred. Please check the log for more details.")


if __name__ == "__main__":
    main()
