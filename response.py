# import the necessary libraries
# validate email address as per the validator_collection documentation
# from PyPI https://pypi.org/project/validator-collection/

from validator_collection import validators, checkers, errors


try:
    # get the email address and validate
    email_address = validators.email(input("What's your email address? "))
    if checkers.is_email(email_address):
        print("Valid email address")
except(errors.InvalidEmailError, errors.EmptyValueError):
    print("Invalid email address")


