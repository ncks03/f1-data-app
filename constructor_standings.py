import requests

import driver_standings


def fetch_constructor_standings():

    url = f'http://ergast.com/api/f1/current/constructorStandings.json'
    constructor_standings = requests.get(url)

    return constructor_standings.json()

def display_constructor_standings():

    # Define current standings
    constructor_leaderboard = fetch_constructor_standings()
    constructor_leaderboard = constructor_leaderboard['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings']

    # Print season
    print(f'Now viewing driver standings from 2024 season:\n')

    # Print header
    header = '%-10s%-25s%-20s%-12s' % ('Position', 'Driver', 'Constructor', 'Points')
    print(header)
    print('-' * len(header))

    # Print results
    for driver in constructor_leaderboard:
        position_text = driver['positionText']
        driver_name = f"{driver['Driver']['givenName']} {driver['Driver']['familyName']}"
        constructor_name = driver['Constructors'][0]['name']
        points = driver['points']

        print('%-10s%-25s%-20s%-12s' % (position_text, driver_name, constructor_name, points))

if __name__ == '__main__':
    display_constructor_standings()