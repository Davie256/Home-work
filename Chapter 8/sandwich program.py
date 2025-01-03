import pyinputplus as py

print('Which type of bread would you like to be served? ')

bread = py.inputMenu(['Wheat', 'White', 'Sourdouh'], numbered = True)

if bread == 'Wheat':
    print('You want Wheat bread, noted \n')
elif bread == 'White':
    print('You want White bread, noted \n')
else:
    print('You want Sourdouh bread, noted \n')

print('Which type of Protein would you like to be served? ')

protein = py.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'], numbered = True)

if protein == 'Chicken':
    print('So you want to be served Chicken protein, Noted \n')
elif protein == 'Turkey':
    print('So you want to be served Turkey protein, Noted \n')
elif protein == 'Ham':
    print('So you want to be served Ham protein, Noted \n')
else:
    print('So you want to be served Tofu protein, Noted \n')

cheese = py.inputYesNo('Do you happen to like Cheese on your Sandwich? \n')

if cheese == 'yes':
    print('What cheese type would you like to be served? ')

    cheese_type = py.inputMenu(['Cheddar', 'Swiss', 'Mozzarella'], numbered = True)

    if cheese_type == 'Cheddar':
        print('So you want Cheddar as your cheese, Noted \n')
    elif cheese_type == 'Swiss':
        print('So you want Swiss as your cheese, Noted \n')
    else:
        print('So you want Mozzarella as your cheese, Noted \n')
else:
    print("So you don't want Cheese on your Sandwich, Noted \n")

supplements = py.inputYesNo('Do you want mayo, mustard, lettuce or tomato on your Sandwich? \n')

if supplements == 'yes':
    print('Okay, they will be added to your sandwich as well. \n')
else:
    print("Okay, they won't be included on your Sandwich. \n")

Total_sandwiches = py.inputInt('How many sandwiches would you like to served? \n', min = 1)
print(f"So you want to be served {Total_sandwiches} sandwiches, Let's go prepare your order Sir!!!")






