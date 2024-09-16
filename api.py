import requests

API_URL = 'http://ergast.com/api/f1'

def fetch_data(endpoint):
    """
    Fetches data from the given API endpoint.

    :param endpoint: The specific endpoint to fetch data from.
    :return: JSON response containing the data or None if an error occurred.
    """
    url = f'{API_URL}/{endpoint}'
    # Try to get data from endpoint
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx and 5xx)
        return response.json()

    # Raise exceptions if there was an error
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except requests.exceptions.RequestException as req_err:
        print(f'Request error occurred: {req_err}')
    return None

# Functions for getting data from given endpoints
def fetch_race_results(season, round):
    endpoint = f'{season}/{round}/results.json'
    return fetch_data(endpoint)

def fetch_season_info(season):
    endpoint = f'{season}.json'
    return fetch_data(endpoint)

def fetch_constructor_standings():
    endpoint = 'current/constructorStandings.json'
    return fetch_data(endpoint)

def fetch_driver_standings():
    endpoint = 'current/driverStandings.json'
    return fetch_data(endpoint)