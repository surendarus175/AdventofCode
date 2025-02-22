# Advent of Code - Puzzle Solutions

This repository contains solutions for the Advent of Code challenges, with each puzzle solution organized into separate folders for `Puzzle1` and `Puzzle2`. Each puzzle contains its own `src`, `resources`, and `test` folders.

## Project Structure

```
AdventofCode/
├── Puzzle1/             # Folder containing the solution for Puzzle 1
│   ├── resources/       # Input files for Puzzle 1
│   ├── src/             # Python source code for Puzzle 1
│   └── test/            # Unit tests for Puzzle 1
├── Puzzle2/             # Folder containing the solution for Puzzle 2
│   ├── resources/       # Input files for Puzzle 2
│   ├── src/             # Python source code for Puzzle 2
│   └── test/            # Unit tests for Puzzle 2
└── README.md            # This file
```

## Features
- Each puzzle solution is self-contained within its own folder (`Puzzle1` and `Puzzle2`).
- The `resources` folder contains input files for each puzzle.
- The `src` folder contains the Python script that implements the solution.
- The `test` folder contains unit tests for validating the solution.

## Requirements
- Python 3.x
- The `logging` module (standard in Python, no need to install)

## Setup

1. Clone the repository or download it to your local machine.
   ```bash
   git clone https://github.com/your-username/AdventofCode.git
   cd AdventofCode
   ```

2. Each puzzle folder (`Puzzle1`, `Puzzle2`) contains a `resources` folder where you should place your input files.

3. Ensure the structure is as follows:
   ```
   AdventofCode/
   ├── Puzzle1/
   │   ├── resources/
   │   ├── src/
   │   └── test/
   ├── Puzzle2/
   │   ├── resources/
   │   ├── src/
   │   └── test/
   ```

## How to Use

### For Puzzle 1:

1. In the terminal, from the root directory (AdventofCode) run the `Solution.py` script as:
   ```bash
   python Puzzle1/src/Solution.py
   ```

2. The script will prompt you to enter the name of the file located in the `resources` folder. For example:
   ```
   Enter the name of the file to read (from 'resources' folder): input.txt
   ```

3. The script will get the first and last digits of each line in the file, then concatenates them and calculates the sum of all the concatenated values and displays the result.

4. If an error occurs, it will be logged, and you can check the log for more details.


## Example

### Input file (`Puzzle1/resources/input.txt`):
```
abc1def2
3gh45ij
6kl
```

### Output:
```
Total sum: 119
```

### How it works:
- On the first line: first digit → 1 and last digit → 2. Then concat both first digit and last digit to get 12.
- On the second line: first digit → 3 and last digit → 5. Then concat both first digit and last digit to get 35.
- On the third line: first digit → 6 and last digit → 6. Then concat both first digit and last digit to get 66.

The total sum = 12 + 35 + 66 = 113.


### For Puzzle 2:

1. In the terminal, from the root directory (AdventofCode) run the `Solution.py` script as:
   ```bash
   python Puzzle2/src/Solution.py
   ```

2. The script will prompt you to enter the name of the file located in the `resources` folder. For example:
   ```
   Enter the name of the file to read (from 'resources' folder): input.txt
   ```

3. The script will get the first and last digits or digit words of each line in the file, then concatenates them and calculates the sum of all the concatenated values and displays the result.
   
4. If an error occurs, it will be logged, and you can check the log for more details.


## Example

### Input file (`Puzzle2/resources/input.txt`):
```
two1nine
eightwothree
abcone2threexyz
```

### Output:
```
Total sum: 125
```

### How it works:
- On the first line: first digit or digit word → 2 (two) and last digit or digit word → 9 (nine). Then concat both first and last digits or digit words to get 29.
- On the second line: first digit or digit word → 8 (eight) and last digit or digit word → 3 (three). Then concat both first and last digits or digit words to get 83.
- On the third line: first digit or digit word → 1 (one) and last digit or digit word → 3 (three). Then concat both first and last digits or digit words to get 13.

The total sum = 29 + 83 + 13 = 125.


## Testing

Each puzzle folder contains a `test` folder with unit tests for validating the solution. To run the tests for both Puzzle1 and Puzzle2 solutions, run the following commands:
```bash
python -m unittest Puzzle1/test/SolutionTest.py
python -m unittest Puzzle2/test/SolutionTest.py
```

## Error Handling

- **FileNotFoundError**: Logs an error if the file specified is not found.
- **IOError**: Catches input/output errors during file reading.
- **General Exception**: Any unexpected errors will be logged with traceback information.
```
