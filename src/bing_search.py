import requests


class BingSearch:

    subscription_key = "..."
    search_url = "https://api.bing.microsoft.com/v7.0/search"
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}

    @classmethod
    def bing_search(cls, search_term: str) -> list[str]:
        params = {"q": search_term, "textDecorations": True, "textFormat": "HTML"}
        response = requests.get(cls.search_url, headers=cls.headers, params=params)
        response.raise_for_status()
        search_results = response.json()

        return [result["url"] for result in search_results["webPages"]["value"]]
