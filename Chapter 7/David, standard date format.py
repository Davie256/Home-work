import re

print('1. MM/DD/YYYY \n2. DD/MM/YYYY \n3. YYYY/MM/DD \n')

date_format = int(input('Enter the format digit you want to use ie. 1,2,3: \n '))

if 1<=date_format<=3:
    user_date = input('\nEnter the date to be changed to the standard format: \n')

    if date_format == 1:
        pattern_1 = re.compile(r'(0[1-9]|1[012])/(0[1-9]|1[0-9]|2[0-9]|3[01])/([12][0-9]{3})')

        for date in user_date:
            match = re.match(pattern_1, user_date)

            if match:
               month, day, year = match.groups()

               day = int(day)
               month = int(month)
               year = int(year)

               print(f'\nThe standard date format of {user_date} is: \n')
               print(year, end= '/')
               print(month, end = '/')
               print(day)
               break

            else:
                print(f'\n{user_date} doesnot match the selected option')
                break

    elif date_format == 2:
        pattern_2 = re.compile(r'(0[1-9]|1[0-9]|2[0-9]|3[01])/(0[1-9]|1[012])/([12][0-9]{3})')

        for date in user_date:
            match = re.match(pattern_2, user_date)

            if match:
               day, month, year = match.groups()

               day = int(day)
               month = int(month)
               year = int(year)

               print(f'\nThe standard date format of {user_date} is: \n')
               print(year, end= '/')
               print(month, end = '/')
               print(day)
               break

            else:
                print(f'\n{user_date} doesnot match the selected option')
                break

    else:
        pattern_3 = re.compile(r'([12][0-9]{3})/(0[1-9]|1[012])/(0[1-9]|1[0-9]|2[0-9]|3[01])')

        for date in user_date:
            match = re.match(pattern_3, user_date)

            if match:
               year, month, day  = match.groups()

               day = int(day)
               month = int(month)
               year = int(year)

               print(f'\nThe date {user_date} is already in the standard date format \n')
               break

            else:
                print(f'\n{user_date} doesnot match the selected option')
                break

else:
    print(f'\n{date_format} is not among the provided options')
