import requests

import driver_standings


def fetch_constructor_standings():

    url = f'http://ergast.com/api/f1/current/constructorStandings.json'
    constructor_standings = requests.get(url)

    return constructor_standings.json()

def display_constructor_standings():

    # Define current standings
    constructor_leaderboard = fetch_constructor_standings()

    print(constructor_leaderboard)
    constructor_leaderboard = constructor_leaderboard['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings']

    # Print season
    print(f'Now viewing driver standings from 2024 season:\n')

    # Print header
    header = '%-10s%-25s%-20s%-12s' % ('Position', 'Driver', 'Constructor', 'Points')
    print(header)
    print('-' * len(header))

    # Print results
    for constructor in constructor_leaderboard:
        position_text = constructor['positionText']
        constructor_name = constructor['Constructor']['name']
        nationality = constructor['Constructor']['nationality']
        points = constructor['points']

        print('%-10s%-25s%-20s%-12s' % (position_text, constructor_name, nationality, points))

if __name__ == '__main__':
    display_constructor_standings()