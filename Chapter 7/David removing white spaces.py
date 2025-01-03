import re

text = input('Enter any sentence you feel like: \n')

remove_space = re.sub(r'\s+','', text)
print(remove_space)
