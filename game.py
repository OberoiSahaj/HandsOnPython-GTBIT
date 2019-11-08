import random

options = ['stone','paper','scissors']

user = None

while True:
    
    user = input('Enter Stone, Paper or Scissors:  ')
    user = user.lower()

    if user == 'exit':
        break
    
    comp = random.choice(options)

    if user not in options:
        user = input('Invalid option. Enter again: ')
    if comp == 'stone' and user == 'paper':
        print('Computer chose Stone, so you Win')        
    elif comp == 'stone' and user == 'scissors':
        print('Computer chose Stone, so you Lose')
    elif comp == 'stone' and user == 'stone':
        print('Computer chose Stone, so it is a Tie')
                    
    if comp == 'paper' and user == 'paper':
        print('Computer chose Paper, so it is a Tie')
    elif comp == 'paper' and user == 'scissors':
        print('Computer chose Paper, so you Win')
    elif comp == 'paper' and user == 'stone':
        print('Computer chose Paper, so you Lose')
                    
    if comp == 'scissors' and user == 'scissors':
        print('Computer chose Scissors, so it is a Tie')
    elif comp == 'scissors' and user == 'stone':
        print('Computer chose Scissors, so you Win')
    elif comp == 'scissors' and user == 'paper':
        print('Computer chose Scissors, so you Lose')
