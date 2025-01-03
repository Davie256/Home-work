import re

pattern = re.compile(r'(0[1-9]|1[0-9]|2[0-9]|3[01])/(0[1-9]|1[012])/([12][0-9]{3})')

text = input('Enter the date to be checked in DD/MM/YYYY format: \n')

for date_str in text:
    match = re.match(pattern, text) #Here am matching the user text with the regex

    if match:
        day, month, year = match.groups() #Assigning the different groups to variable names

        day = int(day)    #Changing the the user input from string format to interger format
        month = int(month)
        year = int(year)

        month_lists = [[2],[4,6,9,11],[1,3,5,7,8,10,12]]
        #Grouping the lists of list depending on the number of dates they contain


        valid_day_1 = (day<=30 and month in month_lists[1])
        valid_day_2 = (day<=29 and month in month_lists[0] and (year % 4==0 and (year % 100 != 0 or year % 400==0)))
        valid_day_3 = (day<=31 and month in month_lists[2])
        #Creating conditions for validity of the the date

        if valid_day_1 or valid_day_2 or valid_day_3 is True:
            print(f'\n{text} is a VALID DATE')
            break
        else:
            print(f'\n{text} is an INVALID DATE !!!')
            break

    else:
        print(f'\n{text} doesnot match the expected date format !!!')
        break
