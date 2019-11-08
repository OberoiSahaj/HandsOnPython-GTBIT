import random

options = ['stone','paper','scissor']

comp = random.choice(options)

user = None

while user != 'exit':

    comp = random.choice(options)
    user = input('Enter stone, paper or scissor:  ')
    user = user.lower()
    if user not in options:
        user = input('Invalid option. Renter: ')

    if comp == 'stone' and user == 'paper':
        print('You win')
        
    elif comp == 'stone' and user == 'scissor':
        print('You lose')
    elif comp == 'stone' and user == 'stone':
        print('It is a tie')
    
    if comp == 'paper' and user == 'paper':
        print('It is a tie')
    elif comp == 'paper' and user == 'scissor':
        print('You win')
    elif comp == 'paper' and user == 'stone':
        print('You lose')
    
    if comp == 'scissor' and user == 'scissor':
        print('It is a tie')
    elif comp == 'scissor' and user == 'stone':
        print('You win')
    elif comp == 'scissor' and user == 'paper':
        print('You lose')