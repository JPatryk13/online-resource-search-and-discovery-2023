import requests
from bs4 import BeautifulSoup


def whois_api_search(website_name: str) -> None:
    page = requests.get(f"https://who.is/whois/{website_name}")
    soup = BeautifulSoup(page.content, "html.parser")
    sections = soup.find_all("div", class_="rawWhois")

    for section in sections:
        rows = section.find_all("div", class_="row")
        for row in rows:
            print(row.text.strip())
            
if __name__ == '__main__':
    whois_api_search('...')
