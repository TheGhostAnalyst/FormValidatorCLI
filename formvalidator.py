import re
phone_regex = re.compile(
    r'^(\+?\d{1,3}[\s-]?)?'         # optional country code
    r'(\(?\d{2,4}\)?[\s-]?)?'       # optional area code
    r'\d{3,4}[\s-]?\d{4}$'          # main number
)
phone_regex = re.compile(r'(?:[^0]\(?\+?\d{1,3}?\)?\s?\-?)?(?:\(?\d{2,4}\)?[\s.-]?)?\(?\d{3,4}\)?[\s.-]?\(?\d{4}\)?')
email_regex = re.compile(r'[a-zA-Z0-9_.+-]+@[a-z0-9-.]+\.[a-zA-Z0-9-]+', re.IGNORECASE)
fullname_regex = re.compile(r'^[A-Za-z]+(?: [A-Za-z]+)+$')
dob = re.compile(r'\d{4}[/.-]\d{1,2}[/.-]\d{1,2}')
pass_reg = re.compile(r'[a-zA-Z0-9@#^%&*+=!]{8,}')
linkreg = re.compile(
    r'(https?://)?'               # optional http or https scheme
    r'(www\.)?'                   # optional www.
    r'([\w\-]+\.)+'               # one or more domain parts (subdomain.domain.)
    r'[a-zA-Z]{2,}'               # top-level domain (.com, .co.uk etc)
    r'(/[^\s]*)?'                 # optional path and query after slash
)

details = {'name': '', 'email': '', 'dob': '', 'phone': '', 'link': '', 'password': ''}


def validate_input(prompt, regex, error_msg):
    while True:
        value = input(prompt)
        if not regex.fullmatch(value):
            print(error_msg)
        else:
            return value

print("Form validation Testing Application")

details['name'] = validate_input(
    "Enter your full name: ",
    fullname_regex,
    "Invalid name format. Please enter a valid full name."
)
print("Valid name format.\nName added to details.\n")

details['email'] = validate_input(
    "Enter your email address: ",
    email_regex,
    "Invalid email format. Please enter a valid email address."
)
print("Valid email format.\nEmail added to details.\n")

details['dob'] = validate_input(
    "Enter your date of birth (YYYY-MM-DD): ",
    dob,
    "Invalid date format. Please enter a valid date in YYYY-MM-DD format."
)
print("Valid date format.\nDate of birth added to details.\n")

details['phone'] = validate_input(
    "Enter your phone number: ",
    phone_regex,
    "Invalid phone number format. Please enter a valid phone number."
)
print("Valid phone number format.\nPhone number added to details.\n")

details['link'] = validate_input(
    "Enter a your website valid link: ",
    linkreg,
    "Invalid link format. Please enter a valid link."
)
print("Valid link format.\nLink added to details.\n")

details['password'] = validate_input(
    "Enter your password: ",
    pass_reg,
    "Invalid password format. Password must be at least 8 characters long and can include letters, numbers, and special characters (@#^%&*+=!)."
)
print("Valid password format.\nPassword added to details.")

print("\nForm validation completed successfully!\n")
print("Details collected:")
for key, value in details.items():
    print(f"{key.upper()}: {value}")
print("\nThank you for using the form validation application!")
