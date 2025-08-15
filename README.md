````markdown
# Form Validation CLI (Python + PyInputPlus)

A simple **Command-Line Interface (CLI) application** in Python that validates user inputs using **PyInputPlus** and **regular expressions (regex)**. This project demonstrates best practices for input validation, error handling, and user-friendly prompts in Python.

## Features

- Validates **Full Name**, **Email**, **Date of Birth**, **Phone Number**, **Website URL**, and **Password**.
- Custom error messages for invalid inputs.
- Limits user retries to prevent infinite loops.
- Handles blank inputs gracefully.
- Modular and easily extendable for new fields or validation rules.

## Requirements

- Python 3.X
- [PyInputPlus](https://pypi.org/project/PyInputPlus/)

```bash
pip install pyinputplus
````

## Usage

1. **Clone the repository:**

```bash
git clone https://www.FormValidatorCLI.git
cd FormValidatorCLI
```

2. **Run the script:**

```bash
python form_validation.py
```

### Example Interaction

```
Enter your full name: John Doe
Enter your email address: john.doe@example.com
Enter your date of birth (YYYY-MM-DD): 2000-05-21
Enter your phone number: +234 802-123-4567
Enter your website link: https://example.com
Enter your password: StrongP@ss1
```

**Output:**

```
Form validation completed successfully!

Details collected:
NAME: John Doe
EMAIL: john.doe@example.com
DOB: 2000-05-21
PHONE: +234 802-123-4567
LINK: https://example.com
PASSWORD: StrongP@ss1
```

## How it Works

* Uses **`allowRegexes`** to accept only valid inputs.
* Uses **`blockRegexes`** with custom messages for invalid entries.
* Ensures blank inputs are rejected with **`blank=False`**.
* Limits retries with **`limit=3`**.
* Handles date input with **`pyip.inputDate()`** and specified formats.

## Contributing

Feel free to fork and extend this project. You can add more fields, improve regex patterns, or enhance error handling.

## License

MIT License

