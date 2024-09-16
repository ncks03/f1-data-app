import api
    
def display_driver_standings():
    """
    Displays the current driver standings
    :return:
    """
    # Define current standings
    driver_standings = api.fetch_driver_standings()
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