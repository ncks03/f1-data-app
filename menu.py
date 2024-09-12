# Imports
from results import display_race_results
from race_schedule import display_race_schedule
from driver_standings import display_driver_standings
from constructor_standings import display_constructor_standings

# Menu function
def main_menu():
    # Infinite while loop for main menu
    while True:
        menu_stop = False

        print(
            f'Welcome to the f1 data app\n'
            f'You can choose from the following functionalities:\n'
            f'\t1. Race schedule\n'
            f'\t2. Results from previous race\n'
            f'\t3. Current driver standings\n'
            f'\t4. Current team standings\n'
        )

        # User chooses what they want to see
        choice = input('Input you choice number: \n')

        # If statement to call chosen function
        if choice == '1':
            display_race_schedule()

        elif choice == '2':
            display_race_results()

        elif choice == '3':
            display_driver_standings()

        elif choice == '4':
            display_constructor_standings()

        else:
            print(f'Choice \'{choice}\' doesn\'t exist. Please try again.')
            choice = input('Input your choice number: \n')
            continue

        # While loop for choice to continue
        while True:
            cont = input(f'\nDo you want to make another choice? (yes/no) ')

            cont = cont.lower()

            if cont == 'yes':
                menu_stop = False
                break
            elif cont == 'no':
                menu_stop = True
                break
            else:
                print(f'\'{choice}\' isn\'t a valid choice. Please enter yes or no.')
                cont = input('Do you want to make another choice? (yes/no) ')
                continue

        if menu_stop == False:
            continue
        elif menu_stop == True:
            break

if __name__ == '__main__':
    main_menu()