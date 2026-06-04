import re
import requests
from bs4 import BeautifulSoup

def fetch_google_doc_content(doc_url):
    response = requests.get(doc_url)
    response.raise_for_status()
    return response.text


def print_html_parser(content):
    soup = BeautifulSoup(content, "html.parser")

    table = soup.find("table")

    if not table:
        print("No table found")
        return

    rows = table.find_all("tr")

    data = []

    for row in rows:
        cols = row.find_all(["td", "th"])
        cols = [col.get_text(strip=True) for col in cols]

        if cols:
            data.append(cols)
        
    data.pop(0)

    data.sort(key=lambda x: (int(x[2]), int(x[0])))

    return data

def print_secret(data):
    
    max_x = max(int(row[0]) for row in data)
    max_y = max(int(row[2]) for row in data)

    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, ch, y in data:
        x = int(x)
        y = int(y)
        grid[y][x] = ch

    for row in reversed(grid):
        print(''.join(row))

url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
# url = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"
try:
    content = fetch_google_doc_content(url)
    coordinates = print_html_parser(content)
    print_secret(coordinates)
except Exception as e:
    print(f"Error: {e}")
