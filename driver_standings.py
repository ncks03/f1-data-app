import requests

API_URL = 'http://ergast.com/api/f1'

def fetch_driver_standings():
    """
    Calls API to fetch driver standings
    :return response:
    """
    url = API_URL + '/current/driverStandings.json'
    try:
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f'Error fetching driver standings: status code {response.status_code}')
            return None
        else:
            return response.json()

    except requests.exceptions.RequestException as e:
        print(f'Something went wrong: {e}')
        return None
    
def display_driver_standings():
    """
    Displays the current driver standings
    :return:
    """
    # Define current standings
    driver_standings = fetch_driver_standings()
    driver_leaderboard = driver_standings['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']

    # Print season
    print(f'Now viewing driver standings from 2024 season:\n')

    # Print header
    header = '%-10s%-25s%-20s%-12s' % ('Position', 'Driver', 'Constructor', 'Points')
    print(header)
    print('-' * len(header))

    # Print results
    for driver in driver_leaderboard:
        position_text = driver['positionText']
        driver_name = f"{driver['Driver']['givenName']} {driver['Driver']['familyName']}"
        constructor_name = driver['Constructors'][0]['name']
        points = driver['points']

        print('%-10s%-25s%-20s%-12s' % (position_text, driver_name, constructor_name, points))

if __name__ == '__main__':
    display_driver_standings()