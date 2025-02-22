import logging
import os

# Configure logging to capture errors and other log messages
logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")


def extract_and_sum(file_path: str) -> int:
    """
    Extracts the first and last digits from each line of the specified file,
    concatenates them, and sums up the resulting integers.

    Args:
    - file_path (str): Path to the input file containing the lines with digits.

    Returns:
    - int: The sum of the concatenated first and last digits across all lines in the file.
    - None: If an error occurs, such as file not found or I/O error.
    """
    total_sum = 0

    try:
        # Open the file and process each line
        with open(file_path, "r") as file:
            for line in file:
                first_digit = last_digit = None

                # Identify the first and last digits in the line
                for char in line:
                    if char.isdigit():
                        if first_digit is None:
                            first_digit = char  # Capture the first digit
                        last_digit = char  # Update the last digit

                # If both first and last digits are found, concatenate them and add to the total sum
                if first_digit is not None and last_digit is not None:
                    total_sum += int(first_digit + last_digit)

    except FileNotFoundError:
        logging.error(f"File '{file_path}' not found.")
        return None
    except IOError as io_error:
        logging.error(f"I/O error occurred while accessing the file '{file_path}': {io_error}")
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
    result = extract_and_sum(file_path)

    if result is not None:
        print(f"Total sum: {result}")
    else:
        print("An error occurred. Please check the log for more details.")


if __name__ == "__main__":
    main()
