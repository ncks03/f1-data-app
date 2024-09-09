import requests

def get_results():

    race_results = requests.get('http://ergast.com/api/f1/current/last/results.json')

    print(race_results.json())

if __name__ == '__main__':
    get_results()