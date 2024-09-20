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
        response.raise_for_status()  # Raises HTTPError for bad responses
        return response.json()

    # Raise exceptions if there was an error
    except requests.exceptions.HTTPError as http_error:
        print(f'HTTP error occurred: {http_error}')
    except requests.exceptions.RequestException as req_error:
        print(f'Request error occurred: {req_error}')
    return None

# Functions for getting data from given endpoints
def fetch_race_results(season, round):
    """
    Fetches race results for the given season and round.
    :return data as json:
    """
    endpoint = f'{season}/{round}/results.json'
    return fetch_data(endpoint)

def fetch_season_info(season):
    """
    Fetches information about the given season.
    :return data as json:
    """
    endpoint = f'{season}.json'
    return fetch_data(endpoint)

def fetch_constructor_standings():
    """
    Fetches constructor standings.
    :return data as json:
    """
    endpoint = 'current/constructorStandings.json'
    return fetch_data(endpoint)

def fetch_driver_standings():
    """
    Fetches driver standings.
    :return data as json:
    """
    endpoint = 'current/driverStandings.json'
    return fetch_data(endpoint)