# Square Root Bisection Method

## Overview
This Python project calculates the square root of a given number using the bisection method. The bisection method is an iterative algorithm that finds the square root by repeatedly dividing the search interval in half and narrowing down to the target value.

## Features
- **Handles Edge Cases**: Returns 0 for an input of 0 and 1 for an input of 1. It raises an error for negative inputs.
- **Adjustable Parameters**: Allows fine-tuning of precision (`tolerance`) and maximum iterations (`max_iterations`).
- **Efficient Calculation**: Approximates square roots for positive numbers with high accuracy.
- **Error Handling**: Provides a message if the algorithm fails to converge within the allowed iterations.

## Usage
### Requirements
- Python 3.x installed on your system.

### Example Usage
1. Run the script.
2. Enter a number when prompted.
3. The script calculates and prints the approximate square root.

#### Input
```text
Enter any number to get square root: 25
```

#### Output
```text
The square root of 25 is approximately 5.0
```

### Edge Cases
- Input: `0`
  ```text
  The square root of 0 is 0
  ```
- Input: `1`
  ```text
  The square root of 1 is 1
  ```
- Input: `-4`
  ```text
  ValueError: Square root of negative number is not defined in real numbers
  ```

## How It Works
1. **Initialization**:
   - For numbers greater than 1, sets `low` to 0 and `high` to the input number.
   - For numbers less than 1, sets `low` to 0 and `high` to 1.
2. **Iteration**:
   - Calculates the midpoint of `low` and `high`.
   - Squares the midpoint and compares it to the target.
   - Narrows the interval based on whether the square is less than or greater than the target.
3. **Termination**:
   - Stops if the square is within the specified tolerance or the maximum iterations are reached.
4. **Result**:
   - Returns the calculated square root or an error message if convergence fails.

