# Write your code here :-)
import random
guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

if guess == 'heads':
    guess = 1
else:
    guess = 0

toss = random.randint(0, 1) # 0 is tails, 1 is heads

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    if toss == guesss:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
