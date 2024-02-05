import requests
import json
import os


def google_search(query: str, page: int) -> None:
    # constructing the URL; doc: https://developers.google.com/custom-search/v1/using_rest
    # calculating start starting element of the search
    start = (page - 1) * 10 + 1
    url = f"https://www.googleapis.com/customsearch/v1?key={os.environ.get('API_KEY')}&cx={os.environ.get('SEARCH_ENGINE_ID')}&q={query}&start={start}"

    # make the API request
    data = requests.get(url).json()

    print(data)
        
        
if __name__ == '__main__':
    google_search('sample', 1)