from logging import raiseExceptions

import requests

def fetch_race_results(season, round):

    # Fetch results from ergast API
    race_results = requests.get(f'http://ergast.com/api/f1/{season}/{round}/results.json')

    return race_results

def display_race_results():

    # Which season does the user want results from
    season = int(input('Which season do you want race results from? '))

    # Print number of rounds in season for ease of use
    number_of_races = requests.get(f'http://ergast.com/api/f1/{season}.json')
    print(f'The {season} season has {len(number_of_races.json()['MRData']['RaceTable']['Races'])} rounds')

    # Which round does the user want results from
    round = int(input('Which round do you want race results from? '))

    # Raise error when user chooses round that doesn't exist in chosen season
    if round > len(number_of_races.json()['MRData']['RaceTable']['Races']):
        raise Exception(f'The {season} season does not have a round {round}')

    # Define results in dictionaries
    race_results = fetch_race_results(season, round).json()
    race_info_dict = race_results['MRData']['RaceTable']['Races'][0]
    race_results_dict = race_results['MRData']['RaceTable']['Races'][0]['Results']

    # Check if results is a dictionary
    if type(race_results) == dict:
        # Print info about results
        print(f'Now viewing results from {season} season, round {round}:\n'
              f'\n'
              f'Race Name: \t {race_info_dict['raceName']}\n'
              f'Circuit: \t {race_info_dict['Circuit']['circuitName']}\n'
              f'City: \t\t {race_info_dict['Circuit']['Location']['locality']}\n')

        # Print header
        header = '%-12s%-25s%-20s%-12s' % ('Position', 'Driver', 'Constructor', 'Interval')
        print(header)
        print('-' * len(header))

        # Print results
        for driver in race_results_dict:
            position_text = driver['positionText']
            driver_name = f"{driver['Driver']['givenName']} {driver['Driver']['familyName']}"
            constructor_name = driver['Constructor']['name']
            interval = driver.get('Time', {}).get('time', 'N/A')

            print('%-12s%-25s%-20s%-12s' % (position_text, driver_name, constructor_name, interval))
    else:
        print('Invalid season or round!')

# Test functions
if __name__ == '__main__':
    display_race_results()