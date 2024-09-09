import requests

def get_results():

    race_results = requests.get('http://ergast.com/api/f1/current/last/results')