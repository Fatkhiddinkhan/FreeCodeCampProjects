# Building a Password Generator

## Overview
This Python project is a secure and customizable password generator that creates strong passwords with user-specified constraints. It ensures the generated password meets specific criteria such as the inclusion of uppercase letters, lowercase letters, numbers, and special characters.

## Features
- **Customizable Length**: Set the desired length of the password.
- **Constraint Validation**: Ensure the password contains a minimum number of numbers, special characters, uppercase, and lowercase letters.
- **Secure Generation**: Uses Python's `secrets` module for cryptographically secure random password generation.
- **Flexible Defaults**: Default parameters ensure a balanced, secure password if no customization is provided.

## Why is it Helpful?
- **Improves Security**: Generates strong passwords resistant to brute-force attacks.
- **Customizable**: Meets specific requirements for different platforms or personal preferences.
- **Simple to Use**: Straightforward function with meaningful defaults and outputs.

## How to Use
### Requirements
- Python 3.x installed on your machine.

### Example Usage
1. Run the script.
2. The script generates a password with default parameters (length 16, includes at least 1 number, 1 special character, 1 uppercase letter, and 1 lowercase letter).

#### Default Example
```text
Generated password: H3$t!Kl7#VqP2R*a
```

3. Customize the password by calling the function with your preferred parameters:
   ```python
   generate_password(length=12, nums=2, special_chars=2, uppercase=3, lowercase=3)
   ```

#### Customized Example Output
```text
Generated password: Ab3@cD4!gH5*
```

### Constraints
- The password must meet the minimum requirements specified in the function arguments:
  - `nums`: Minimum number of numeric digits.
  - `special_chars`: Minimum number of special characters.
  - `uppercase`: Minimum number of uppercase letters.
  - `lowercase`: Minimum number of lowercase letters.

## License
This project is open-source and can be used, modified, and distributed under the MIT License.

## Contact
For any questions or feedback, feel free to reach out to [fatkhiddinkhan@gmail.com](mailto:fatkhiddinkhan@gmail.com).

---

Let me know if you'd like to improve or refine any part of this description!
