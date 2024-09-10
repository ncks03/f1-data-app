import requests

def fetch_race_schedule(season):

    race_schedule = requests.get(f'http://ergast.com/api/f1/{season}')

    return race_schedule.json()

def display_race_schedule():

    # Ask user which year's schedule they want to view
    year_choice = input('For which year would you like to see the race schedule?\n')
    race_schedule_dict = fetch_race_schedule(year_choice)

