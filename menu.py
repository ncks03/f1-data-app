# Imports
from results import display_race_results
from race_schedule import display_race_schedule
from driver_standings import display_driver_standings
from constructor_standings import display_constructor_standings

# Menu function
def main_menu():
    """
    This is the main menu of the application. This function requires input from the user and calls the right function.
    """
    # Infinite loop for main menu
    while True:
        # define menu_stop variable so user can stop loop
        menu_stop = False

        # Print options
        print(
            f'\nWelcome to the f1 data app\n'
            f'You can choose from the following functionalities:\n'
            f'\t1. Race schedule\n'
            f'\t2. Results from previous race\n'
            f'\t3. Current driver standings\n'
            f'\t4. Current team standings\n'
        )

        # User chooses what they want to see
        user_choice = input('Input you choice number: \n')

        # If statement to call chosen function
        if user_choice == '1':
            display_race_schedule()

        elif user_choice == '2':
            display_race_results()

        elif user_choice == '3':
            display_driver_standings()

        elif user_choice == '4':
            display_constructor_standings()

        else:
            print(f'Choice \'{user_choice}\' doesn\'t exist. Please try again.')
            continue

        # While loop for choice to continue
        while True:
            continue_choice = input(f'\nDo you want to make another choice? (yes/no) ')

            continue_choice = continue_choice.lower()

            if continue_choice == 'yes' or continue_choice == 'y':
                menu_stop = False
                break
            elif continue_choice == 'no' or continue_choice == 'n' or continue_choice == 'quit':
                menu_stop = True
                break
            else:
                print(f'\'{user_choice}\' isn\'t a valid choice. Please enter yes or no.')
                continue

        # Check if user wants to continue
        if not menu_stop:
            continue
        elif menu_stop:
            break

if __name__ == '__main__':
    main_menu()