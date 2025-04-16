import requests
from bs4 import BeautifulSoup

def fetch_top_10_languages():
    url = "https://www.tiobe.com/tiobe-index/"
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch data from TIOBE website.")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'table table-striped table-top20'})
    if not table:
        print("Failed to locate the table on the TIOBE page.")
        return
    
    
    rows = table.find_all('tr')[1:11]  # Skip the header row and get the top 10 rows
    print("Top 10 Programming Languages (TIOBE Index):")
    for row in rows:
        columns = row.find_all('td')
        rank = columns[0].text.strip()
        language = columns[4].text.strip()  # Corrected to fetch the language name
        rating = columns[5].text.strip()   # Corrected to fetch the rating
        print(f"{rank}. {language} - {rating}")

if __name__ == "__main__":
    fetch_top_10_languages()