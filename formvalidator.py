import re
import sys
import pyinputplus as pyip
# Regular expressions for validating various inputs
phone_regex = re.compile(
    r'^(\+?\d{1,3}[\s-]?)?'         # optional country code
    r'(\(?\d{2,4}\)?[\s-]?)?'       # optional area code
    r'\d{3,4}[\s-]?\d{4}$'          # main number
)
email_regex = re.compile(r'[a-zA-Z0-9_.+-]+@[a-z0-9-.]+\.[a-zA-Z0-9-]+', re.IGNORECASE)
fullname_regex = re.compile(r'^[A-Za-z]+(?: [A-Za-z]+)+$')
pass_reg = re.compile(r'[a-zA-Z0-9@#^%&*+=!]{8,}')
linkreg = re.compile(
    r'(https?://)?'               # optional http or https scheme
    r'(www\.)?'                   # optional www.
    r'([\w\-]+\.)+'               # one or more domain parts (subdomain.domain.)
    r'[a-zA-Z]{2,}'               # top-level domain (.com, .co.uk etc)
    r'(/[^\s]*)?'                 # optional path and query after slash
)

details = {}


try:
    print("Form validation Testing Application")

    details['name'] = pyip.inputStr(
    prompt="Enter your full name: ",
    allowRegexes=[fullname_regex],
    blockRegexes=[(r'.*', "Invalid name format. Please enter a valid full name.")],
    blank=False,
    limit=3
    )
    print("Valid name format.\nName added to details.\n")

    details['email'] = pyip.inputStr(
    prompt="Enter your email address: ",
    allowRegexes=[email_regex],
    blockRegexes=[(r'.*', "Invalid email format. Please enter a valid email address.")],
    blank=False,
    limit=3
    )
    print("Valid email format.\nEmail added to details.\n")

    details['dob'] = pyip.inputDate(
    prompt="Enter your date of birth (YYYY-MM-DD): ",
    formats=[r"%Y-%m-%d"],
    blank=False,
    limit=3
    )
    print("Valid date format.\nDate of birth added to details.\n")

    details['phone'] = pyip.inputNum(
    prompt="Enter your phone number: ",
    allowRegexes=[phone_regex],
    blockRegexes=[(r'.*', "Invalid phone number format. Please enter a valid phone number.")],
    blank=False,
    limit=3
    )
    print("Valid phone number format.\nPhone number added to details.\n")

    details['link'] = pyip.inputStr(
    prompt="Enter a your website valid link: ",
    allowRegexes=[linkreg],
    blockRegexes=[(r'.*', "Invalid link format. Please enter a valid link.")],
    blank=False, limit=3
    )
    print("Valid link format.\nLink added to details.\n")

    details['password'] = pyip.inputStr(
    prompt="Enter your password: ",
    allowRegexes=[pass_reg],
    blockRegexes=[(r'.*', "Invalid password format. Password must be at least 8 characters long and can include letters, numbers, and special characters (@#^%&*+=!).")],
    blank=False,
    limit=3
    )
except pyip.RetryLimitException:
    print("You have exceeded the maximum number of attempts. Exiting the application.")
    sys.exit(1)
except KeyboardInterrupt:
    print("\nApplication interrupted by user. Exiting gracefully.")
    sys.exit(0)
print("Valid password format.\nPassword added to details.")

print("\nForm validation completed successfully!\n")
print("Details collected:")
for key, value in details.items():
    print(f"{key.upper()}: {value}")
print("\nThank you for using the form validation application!")
