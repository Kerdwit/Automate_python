#!python3

#Strong Password detecttion -- JARUWIT KERDPHRA

"""
Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong
password is defined as one that is at least eight characters long, contains both uppercase and lowercase
characters, and has at least one digit. You may need to test the string against multiple regex patterns to
validate its strength.

"""
import re

# Create a regex object for detection password
def TestPassword(pw):
    passwordRegex = re.compile(r'([a-zA-Z0-9]){8,}')
    passwordRegex.search(password)
    if passwordRegex.search(password) == None:
        result = False
    else: result = True
    return result

while True:
    print('Please define your password')
    password = str(input())
    rs = TestPassword(password)
    if rs:
        print('Your password is strength.')
        break
    else: print('Your password is not strength.\nPlease define password again\n')
