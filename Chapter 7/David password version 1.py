import re

while True:
    password = input('Enter your password: \n')
    if len(password)<8:
        print('Your password must have atleast 8 characters !!! ')
        break
    if re.search(r'[A-Z]', password) is None:
        print('Your password must have atleast one uppercase letter !!!')
        break
    if re.search(r'[a-z]', password) is None:
        print('Your password must have atleast one lowercase letter!!!')
        break
    if re.search(r'[0-9]', password) is None:
        print('Your password must have atleast one digit !!!')
        break
    else:
        password2 = input('Comfirm your password: \n')
        if password == password2:
            print('Correct Password')
            break
        else:
            print('This password is different from the first password !!! \n')
