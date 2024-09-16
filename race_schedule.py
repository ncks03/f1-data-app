import requests

API_URL = 'http://ergast.com/api/f1'

def fetch_race_schedule(season):

    url = f'{API_URL}/{season}.json'
    try:
        # Fetch schedule from ergast API
        response = requests.get(f'{API_URL}/{season}.json')
        
        if response.status_code != 200:
            print(f'Something went wrong while fetching data: status code {response.status_code}')
            return None
        else:
            return response.json()

    except requests.exceptions.RequestException as e:
        print(f'Something went wrong while fetching data: {e}')
        return None

def display_race_schedule():

    race_schedule_dict = {}
    season = 0

    # input loop for error handling
    while True:
        try:
            # Ask user which year's schedule they want to view
            season = int(input('For which year would you like to see the race schedule?\n'))
        except ValueError:
            print('Please enter a valid year.')
            continue

        # check if year does not exceed database limits
        if season > 2024:
            print('The database only goes op to 2024, sorry!')
            continue

        # Define race schedule
        race_schedule_dict = fetch_race_schedule(season)
        break

    # Convert race schedule to usable dictionaries
    race_schedule_dict = race_schedule_dict['MRData']['RaceTable']['Races']

    # Print races in season
    print(f'\nThis is the race schedule for the year {season}:\n')

    # Print table header
    header = '%-10s%-30s%-40s%-25s%-12s' % ('Round', 'Race', 'Circuit', 'Location', 'Date')
    print(header)
    print('-' * len(header))

    for race in race_schedule_dict:
        round = race['round']
        race_name = race['raceName']
        circuit = race['Circuit']['circuitName']
        place = f'{race['Circuit']['Location']['locality']}, {race['Circuit']['Location']['country']}'
        date = race['date']

        print('%-10s%-30s%-40s%-25s%-12s' % (round, race_name, circuit, place, date))

if __name__ == '__main__':
    display_race_schedule()







