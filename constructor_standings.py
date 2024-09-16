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