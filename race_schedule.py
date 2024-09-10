import requests

def fetch_race_schedule(season):

    # Fetch schedule from ergast API
    race_schedule = requests.get(f'http://ergast.com/api/f1/{season}.json')

    return race_schedule.json()

def display_race_schedule():

    # Ask user which year's schedule they want to view
    season = input('For which year would you like to see the race schedule?\n')
    race_schedule_dict = fetch_race_schedule(season)

    # Convert race schedule to usable dictionaries
    race_schedule_dict = race_schedule_dict['MRData']['RaceTable']['Races']

    # Print races in season
    print(f'This is the race schedule for the year {season}:\n')

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







