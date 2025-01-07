# Arithmetic Arranger

## Overview
The Arithmetic Arranger is a Python-based utility designed to neatly format and optionally solve simple arithmetic problems. It supports addition and subtraction operations, making it ideal for educational purposes, such as helping students understand basic arithmetic or creating practice problems.

## Features
- **Format Arithmetic Problems:** Neatly arranges arithmetic problems (up to 5 at a time) for easy readability.
- **Supports Two Operations:** Handles addition (`+`) and subtraction (`-`) operations.
- **Optional Answer Display:** Users can choose to display the results of the calculations.
- **Error Handling:** Provides meaningful error messages for invalid input, such as unsupported operators, non-numeric values, or exceeding the maximum problem limit.

## Why is it Helpful?
This tool is especially helpful for:
- **Students**: Simplifies learning arithmetic by providing clear, structured problem formatting.
- **Teachers**: Quickly generates formatted arithmetic problems for practice or exams.
- **Programmers**: Serves as an example project to learn about string manipulation, conditional logic, and functions in Python.

## How to Use
### Requirements
- Python 3.x installed on your machine.

### Usage
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Fatkhiddinkhan/FreeCodeCampProjects.git 
   ```
2. Navigate to the project directory:
   ```bash
   cd Arithmetic-Arranger
   ```
3. Open the Python script in your preferred editor or IDE.
4. Use the `arithmetic_arranger` function to input a list of arithmetic problems. Optionally, include the second parameter (`show_answers`) to display results.
   ```python
   from main import arithmetic_arranger

   print(arithmetic_arranger(["3801 - 2", "123 + 49"], show_answers=True))
   ```

### Output Example
Input:
```python
arithmetic_arranger(["3801 - 2", "123 + 49"], show_answers=True)
```

Output:
```
  3801      123
-    2    +  49
-----    -----
  3799      172
```

### Errors
- **Too Many Problems:** Input more than 5 problems.
- **Invalid Characters:** Use non-numeric characters.
- **Excessive Digits:** Use numbers longer than four digits.
- **Unsupported Operators:** Use operators other than `+` or `-`.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute as needed.

## Contributing
Contributions are welcome! If you find a bug or have suggestions for improvement, please open an issue or submit a pull request.

## Contact
For questions or feedback, please reach out to [fatkhiddinkhan@gmail.com](mailto:fatkhiddinkhan@gmail.com).

---

Add this README to your project for better visibility and understanding of your work. Let me know if you'd like help refining or expanding it!
