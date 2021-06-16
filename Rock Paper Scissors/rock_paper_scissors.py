import random


def user_choice():
    user_inp = input('Please enter your choice (Rock, Paper, Scissors): ').capitalize()
    possible_choices = ['Rock', 'Paper', 'Scissors']
    if user_inp not in possible_choices:
        print('Please enter a Valid Choice')
        user_choice()
    else:
        return user_inp


def computer_choice():
    possible_choices = ['Rock', 'Paper', 'Scissors']
    computer_inp = random.choice(possible_choices)
    return computer_inp


def game_function(user_in, computer_in):
    print('you choose {} and computer choose {} \n'.format(user_in, computer_in))
    if user_in == computer_in:
        print('It is a DRAW! Please try again. \n')
    elif user_in == "Rock":
        if computer_in == "Scissors":
            print("Rock smashes scissors! You win! \n")
        else:
            print("Paper covers rock! You lose. \n")
    elif user_in == "Paper":
        if computer_in == "Rock":
            print("Paper covers rock! You win! \n")
        else:
            print("Scissors cuts paper! You lose. \n")
    elif user_in == "Scissors":
        if computer_in == "paper":
            print("Scissors cuts paper! You win! \n")
        else:
            print("Rock smashes scissors! You lose. \n")


if __name__ == '__main__':
    while True:
        user_input = user_choice()
        computer_input = computer_choice()
        game_function(user_input, computer_input)
        replay = input('Do you wanna play Again (Yes - 1/No - 0): ')
        if replay != '1':
            break

