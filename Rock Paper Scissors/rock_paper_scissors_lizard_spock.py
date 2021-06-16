import random


def user_choice():
    user_inp = input('Please enter your choice (Rock, Paper, Scissors, Lizard, Spock): ').capitalize()
    possible_choices = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    if user_inp not in possible_choices:
        print('Please enter a Valid Choice')
        user_choice()
    else:
        return user_inp


def computer_choice():
    possible_choices = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    computer_inp = random.choice(possible_choices)
    return computer_inp


def game_function(user_in, computer_in):
    winning_rules = {
        'Rock': {'Lizard': 'Rock crushes lizard', 'Scissors': 'Rock crushes scissors'},
        'Paper': {'Spock': 'Paper disproves Spock', 'Rock': 'Paper covers rock'},
        'Scissors': {'Lizard': 'Scissors beheads lizard', 'Paper': 'Scissors cuts paper'},
        'Lizard': {'Spock': 'Lizard poisons Spock', 'Paper': 'Lizard eats paper'},
        'Spock': {'Scissors': 'Spock destroys scissors', 'Rock': 'Spock vaporizes rock'}
    }
    print('you choose {} and computer choose {} \n'.format(user_in, computer_in))
    if user_in == computer_in:
        print('It is a Draw! Please try again.')
    else:
        try:
            print('You Win! ' + winning_rules[user_in][computer_in])
        except KeyError:
            print('You Lose! ' + winning_rules[computer_in][user_in])


while True:
    user_input = user_choice()
    computer_input = computer_choice()
    game_function(user_input, computer_input)
    replay = input('Do you wanna play Again (Yes - 1/No - 0): ')
    if replay != '1':
        break
