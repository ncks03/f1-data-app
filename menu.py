from results import display_race_results
from race_schedule import display_race_schedule
from driver_standings import display_driver_standings
from constructor_standings import display_constructor_standings

# Menu function
def display_menu():
    """
    This is the main menu of the application. This function uses input from the user to call the right functions.
    """
    # define menu_stop variable so user can stop loop
    menu_stop = False

    # Define menu options in tuple
    menu_options = (
        ('Race Schedule', display_race_schedule),
        ('Race Results', display_race_results),
        ('Driver Standings', display_driver_standings),
        ('Constructor Standings', display_constructor_standings),
        ('Exit', None)
    )

    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣔⠒⠀⠉⠉⠢⡀⠀⠀⠀⠀⠀⠀⠀'
        '\n⠀⠀⠀⠀⠀⠀⣀⣀⠠⠄⠒⠘⢿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀'
        '\n⢺⣦⢻⣿⣿⣿⣿⣄⠀⠀⠀⠀⠈⢿⡿⠿⠛⠛⠐⣶⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀'
        '\n⠈⢿⣧⢻⣿⣿⣿⣿⣆⣀⣠⣴⣶⣿⡄⠀⠀⠀⠀⠘⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀'
        '\n⠀⢿⣧⢋⠉⠀⠀⠀⠹⣿⣿⣿⣿⣿⡆⣀⣤⣤⣶⣮⠀⠀⠀⠀⠣⠀⠀⠀⠀'
        '\n⠀⠀⠈⢿⣧⢂⠀⠀⠀⠀⢘⠟⠛⠉⠁⠀⠹⣿⣿⣿⣿⣷⡀⠀⠀⠀⢣⠀⠀⠀'
        '\n⠀⠀⠀⠈⢿⣧⢲⣶⣾⣿⣿⣧⡀⠀⠀⠀⢀⣹⠛⠋⠉⠉⠉⢿⣿⣿⣿⣧⠀⠀'
        '\n⠀⠀⠀⠀⠀⢿⣧⢻⣿⣿⣿⡿⠷⢤⣶⣿⣿⣿⣧⡀⠀⠀⠀⠈⢻⣿⣿⣿⣧⠀'
        '\n⠀⠀⠀⠀⠀⠈⢿⣧⢛⠉⠁⠀⠀⠀⢻⣿⣿⣿⡿⠗⠒⠒⠈⠉⠉⠉⠙⡉⠛⡃'
        '\n⠀⠀⠀⠀⠀⠀⠈⢿⣯⢂⠀⠀⠀⡀⠤⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀'
        '\n⠀⠀⠀⠀⠀⠀⠀⠈⢿⣯⠐⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'
        '\n⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'
        '\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'
        '\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'
        '\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'
        '\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'
        '\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'
        '\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
        '\nWelcome to the F1 data app!')

    # loop for main menu
    while not menu_stop:

        # Print options
        print('\nYou can choose from the following functionalities:\n')
        for index, option in enumerate(menu_options, start=1):
            print(f'{index}: {option[0]}')

        # Let user choose from options
        try:
            # User chooses what they want to see
            user_choice = int(input('\nInput your choice number: \n')) - 1

            choice, action = menu_options[user_choice]

            # Checks if action is empty, then stops program
            if not action:
                menu_stop = True
                break
            # If action is defined, call action as function
            else:
                action()

        except IndexError:
            print(f'Choice {user_choice + 1} does not exist! Please enter a valid choice number')
            continue

        except ValueError:
            print(f'That is not a valid input! Please enter a valid choice number')
            continue

        # Check if user wants to continue
        if not continue_prompt():
            menu_stop = True

def continue_prompt():
    """
    Lets the user choose to continue or to stop
    :return True if user chooses to continue, else False:
    """
    valid_input = {'yes', 'y', 'no', 'n', 'quit', 'exit'}
    while True:
        continue_choice = input(f'\nDo you want to make another choice? (yes/no) ')

        continue_choice = continue_choice.lower()

        # Check if continue_choice is a valid input
        if continue_choice in valid_input:
            # return True if input is yes or y
            return continue_choice in {'yes', 'y'}
        else:
            print(f'Choice \'{continue_choice}\' isn\'t a valid choice. Please enter yes or no.')

if __name__ == '__main__':
    display_menu()