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
    header = f'{'Position':<10}{'Driver':<25}{'Constructor':<20}{'Points':<12}'
    print(header)
    print('-' * len(header))

    # Print results
    for driver in driver_leaderboard:
        position_text = driver['positionText']
        driver_name = f"{driver['Driver']['givenName']} {driver['Driver']['familyName']}"
        constructor_name = driver['Constructors'][0]['name']
        points = driver['points']

        print(f'{position_text:<10}{driver_name:<25}{constructor_name:<20}{points:<12}')

if __name__ == '__main__':
    display_driver_standings()