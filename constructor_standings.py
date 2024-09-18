import api

def display_constructor_standings():
    """
    Displays constructor standings
    """
    # Define current standings
    constructor_standings = api.fetch_constructor_standings()
    constructor_leaderboard = constructor_standings['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings']

    # Print season
    print(f'Now viewing constructor standings from 2024 season:\n')

    # Print header
    header = f'{'Position':<10}{'Constructor':<25}{'Nationality':<20}{'Points':<12}'
    print(header)
    print('-' * len(header))

    # Print results
    for constructor in constructor_leaderboard:
        position_text = constructor['positionText']
        constructor_name = constructor['Constructor']['name']
        nationality = constructor['Constructor']['nationality']
        points = constructor['points']

        print(f'{position_text:<10}{constructor_name:<25}{nationality:<20}{points:<12}')

if __name__ == '__main__':
    display_constructor_standings()