# Solution for Password check

import re
import getpass

def pswd_chk(password):
       print("Validiting the entered password", password)
       if len(password) < 8:
            print("Length of the password is less than 8 characters")
            return False
       if not re.search("[a-z]", password):
        print("Password doesnt have any smaller case alphabets")
        return False
       if not re.search("[A-Z]", password):
        print("Password doesnt have any Upper case alphabets")
        return False
       if not re.search("[0-9]", password):
        print("Password doesnt have any numbers, it should contain atleast 1 number ")
        return False
       if not re.search("[!, @, #, $, %]", password):
        print("Password is missing one of the special characters !, @, #, $, %")
        return False
       return True

        
uname = input('Please enter you User Name ')
# password = input('Please enter your password ')
password = getpass.getpass(prompt='Please enter your password ')

if pswd_chk(password):
    print("Valid Password and is found to be Strong")
else:
    print("Invalid Password")