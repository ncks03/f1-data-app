import requests

API_URL = 'http://ergast.com/api/f1'

def fetch_constructor_standings():

    url = API_URL + '/current/constructorStandings.json'
    try:
        response = requests.get(url)

        if response.status_code != 200:
            print(f'An error occurred while fetching data: status code {response.status_code}')
            return None
        else:
            return response.json()

    except requests.exceptions.RequestException as e:
        print(f'An error occurred while fetching data: {e}')
        return None

def display_constructor_standings():

    # Define current standings
    constructor_standings = fetch_constructor_standings()
    constructor_leaderboard = constructor_standings['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings']

    # Print season
    print(f'Now viewing constructor standings from 2024 season:\n')

    # Print header
    header = '%-10s%-25s%-20s%-12s' % ('Position', 'Constructor', 'Nationality', 'Points')
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