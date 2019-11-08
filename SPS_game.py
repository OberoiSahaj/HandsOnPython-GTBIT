import random

options = ['stone','paper','scissors'] 

user = None

while True: # For continuous loop
    
    user = input('Enter Stone, Paper or Scissors:  ') #Input by user
    user = user.lower()

    if user == 'exit': # If user enters 'exit' then it will come out of loop.
        break
    
    comp = random.choice(options) #Computer chooses it's choice at random

    if user not in options: #if user doesn't enter the desired options
        user = input('Invalid option. Enter again: ')
        
    #Conditions if computer chooses Stone   
    if comp == 'stone' and user == 'paper':
        print('Computer chose Stone, so you Win')        
    elif comp == 'stone' and user == 'scissors':
        print('Computer chose Stone, so you Lose')
    elif comp == 'stone' and user == 'stone':
        print('Computer chose Stone, so it is a Tie')
                    
    #Conditions if computer chooses Paper
    if comp == 'paper' and user == 'paper':
        print('Computer chose Paper, so it is a Tie')
    elif comp == 'paper' and user == 'scissors':
        print('Computer chose Paper, so you Win')
    elif comp == 'paper' and user == 'stone':
        print('Computer chose Paper, so you Lose')
                    
    #Conditions if computer chooses Scissors
    if comp == 'scissors' and user == 'scissors':
        print('Computer chose Scissors, so it is a Tie')
    elif comp == 'scissors' and user == 'stone':
        print('Computer chose Scissors, so you Win')
    elif comp == 'scissors' and user == 'paper':
        print('Computer chose Scissors, so you Lose')
