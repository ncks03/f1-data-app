import api

def display_race_results():
    """
    Takes input for season and round and displays the results of that race
    """
    # Set season to 2024 by default
    season = 2024

    # Which season does the user want results from
    while True:
        # User enters year
        try:
            season = int(input('Which year do you want race results from?\n'))
            break

        # User can try again if they did not enter a valid year
        except ValueError:
            print('Please enter a valid year!')
            continue

    if season > 2024:
        print('The database only goes to season 2024, sorry!')
        return None

    # Print number of rounds in season for ease of use
    season_info = api.fetch_season_info(season)
    if not season_info:
        print('Could not fetch season information.')
        return None

    number_of_races = len(season_info['MRData']['RaceTable']['Races'])
    print(f'The {season} season has {number_of_races} rounds\n')

    # Input loop
    while True:
        # Which round does the user want results from
        round = int(input('Which round do you want race results from?\n'))

        # Raise error when user chooses round that doesn't exist in chosen season
        if round > number_of_races:
            print(f'The {season} season does not have a round {round}')
            continue
        else:
            break

    # Fix for when user inputs round that has not happened yet (2024 season)
    try:
        # Define results in dictionaries
        race_results = api.fetch_race_results(season, round)
        race_info_dict = race_results['MRData']['RaceTable']['Races'][0]
        race_results_dict = race_results['MRData']['RaceTable']['Races'][0]['Results']

    except IndexError:
        print(f'This round has not happened yet or the data is incomplete')
        return None

    # Check if results is a dictionary
    if type(race_results) == dict:
        # Print info about results
        print(f'\nNow viewing results from {season} season, round {round}:\n'
              f'\n'
              f'Race Name: \t {race_info_dict['raceName']}\n'
              f'Circuit: \t {race_info_dict['Circuit']['circuitName']}\n'
              f'City: \t\t {race_info_dict['Circuit']['Location']['locality']}\n')

        # Print header
        header = f'{"Position":<10}{"Driver":<25}{"Constructor":<20}{"Interval":<12}'
        print(header)
        print('-' * len(header))

        # Print results
        for driver in race_results_dict:
            position_text = driver['positionText']
            driver_name = f"{driver['Driver']['givenName']} {driver['Driver']['familyName']}"
            constructor_name = driver['Constructor']['name']
            interval = driver.get('Time', {}).get('time', 'N/A')

            print(f'{position_text:<10}{driver_name:<25}{constructor_name:<20}{interval:<12}')
    else:
        print('Something went wrong!')

# Test functions
if __name__ == '__main__':
    display_race_results()