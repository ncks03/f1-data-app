import requests

API_URL = 'http://ergast.com/api/f1'

def fetch_race_results(season, round):

    url = f'{API_URL}/{season}/{round}/results.json'
    try:
        # Fetch results from ergast API
        response = requests.get(url)

        if response.status_code != 200:
            print(f'An error occurred: status code {response.status_code}')
            return None

        else:
            return response.json()

    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')
        return None

def display_race_results():

    # Which season does the user want results from
    season = int(input('Which season do you want race results from? '))

    if season > 2024:
        print('The database only goes to season 2024, sorry!')
        return None

    # Print number of rounds in season for ease of use
    try:
        number_of_races = requests.get(f'{API_URL}/{season}.json')

        if number_of_races.status_code != 200:
            print(f'An error occurred: status code {number_of_races.status_code}')
            return None

        else:
            print(f'The {season} season has {len(number_of_races.json()['MRData']['RaceTable']['Races'])} rounds')

    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')
        return None

    # Input loop
    while True:
        # Which round does the user want results from
        round = int(input('Which round do you want race results from? '))

        # Raise error when user chooses round that doesn't exist in chosen season
        if round > len(number_of_races.json()['MRData']['RaceTable']['Races']):
            print(f'The {season} season does not have a round {round}')
            continue
        else:
            break

    # Fix for when user inputs round that has not happened yet (2024 season)
    try:
        # Define results in dictionaries
        race_results = fetch_race_results(season, round)
        race_info_dict = race_results['MRData']['RaceTable']['Races'][0]
        race_results_dict = race_results['MRData']['RaceTable']['Races'][0]['Results']

    except IndexError:
        print(f'This round has not happened yet or the data is incomplete')
        return None

    # Check if results is a dictionary
    if type(race_results) == dict:
        # Print info about results
        print(f'Now viewing results from {season} season, round {round}:\n'
              f'\n'
              f'Race Name: \t {race_info_dict['raceName']}\n'
              f'Circuit: \t {race_info_dict['Circuit']['circuitName']}\n'
              f'City: \t\t {race_info_dict['Circuit']['Location']['locality']}\n')

        # Print header
        header = '%-10s%-25s%-20s%-12s' % ('Position', 'Driver', 'Constructor', 'Interval')
        print(header)
        print('-' * len(header))

        # Print results
        for driver in race_results_dict:
            position_text = driver['positionText']
            driver_name = f"{driver['Driver']['givenName']} {driver['Driver']['familyName']}"
            constructor_name = driver['Constructor']['name']
            interval = driver.get('Time', {}).get('time', 'N/A')

            print('%-10s%-25s%-20s%-12s' % (position_text, driver_name, constructor_name, interval))
    else:
        print('Something went wrong!')

# Test functions
if __name__ == '__main__':
    display_race_results()