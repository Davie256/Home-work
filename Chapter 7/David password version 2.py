import re

p = r'[^a-zA-Z0-9]+'

password = input('Enter the password: \n')

if re.search(p, password) is True:
    print('Invalid Password!!!')

else:
    if len(password) >= 8:
        print('Comfirm your password: ')
        password2 = input()
        if password == password2:
            print('Your password has been updated\n')
        else:
            print('This password does not match with the first password\n')
    else:
        print('Your password should have atleast 8 characters\n')

