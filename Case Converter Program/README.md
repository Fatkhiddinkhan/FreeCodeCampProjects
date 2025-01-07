# Snake Case Converter

## Overview
This Python script converts strings from PascalCase or camelCase to snake_case using list comprehensions.

## Features
- Converts PascalCase or camelCase to snake_case.
- Uses list comprehensions for concise and efficient code.

## Usage
1. Pass a PascalCase or camelCase string to the `convert_to_snake_case` function.
2. The function returns the snake_case version of the string.

### Example
Input:
```python
convert_to_snake_case('aLongAndComplexString')
```

Output:
```
a_long_and_complex_string
```

## Code
```python
def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper() else char
        for char in pascal_or_camel_cased_string
    ]
    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('aLongAndComplexString'))

main()
```
