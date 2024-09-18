import api

def display_race_schedule():
    """
    Takes user input to display the chosen season schedule
    """
    # Set default values
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
        race_schedule_dict = api.fetch_season_info(season)
        break

    # Convert race schedule to usable dictionaries
    race_schedule_dict = race_schedule_dict['MRData']['RaceTable']['Races']

    # Print races in season
    print(f'\nThis is the race schedule for the year {season}:\n')

    # Print table header
    header = f'{'Round':<10}{'Race':<30}{'Circuit':<40}{'Location':<25}{'Date':<12}'
    print(header)
    print('-' * len(header))

    # Print every entry in schedule
    for race in race_schedule_dict:
        round = race['round']
        race_name = race['raceName']
        circuit = race['Circuit']['circuitName']
        place = f'{race['Circuit']['Location']['locality']}, {race['Circuit']['Location']['country']}'
        date = race['date']

        print(f'{round:<10}{race_name:<30}{circuit:<40}{place:<25}{date:<12}')

if __name__ == '__main__':
    display_race_schedule()







