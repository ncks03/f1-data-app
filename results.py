from logging import raiseExceptions

import requests

def fetch_race_results(season, round):

    race_results = requests.get(f'http://ergast.com/api/f1/{season}/{round}/results.json')

    return race_results

def display_race_results():

    # Which season does the user want results from
    season = int(input('Which season do you want race results from? '))
    round = int(input('Which round do you want race results from? '))

    race_results = fetch_race_results(season, round).json()
    race_info_dict = race_results['MRData']['RaceTable']['Races'][0]
    race_results_dict = race_results['MRData']['RaceTable']['Races'][0]['Results']

    if type(race_results) == dict:
        print(f'Now viewing results from {season} season, round {round}:\n'
              f'\n'
              f'Race Name: \t {race_info_dict['raceName']}\n'
              f'Circuit: \t {race_info_dict['Circuit']['circuitName']}\n')

    else:
        print('Invalid season or round!')

    print(race_results['MRData']['RaceTable'])



# Test functions
if __name__ == '__main__':
    display_race_results()