import requests
from bs4 import BeautifulSoup


def fetch_news():

    url = "https://www.sec-wiki.com/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Failed to retrieve webpage.")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    content_div = soup.find('div', id='content1')
    news_entries = content_div.find_all('a', attrs={'rev': 'news'})

    news_list = []

    for entry in news_entries:
        news_data = {
            'id': entry['rel'][0] if isinstance(entry['rel'], list) else entry['rel'],
            'date': entry.find_previous('span').text,
            'title': entry.text,
            'link': entry['href'],
            'author': entry.find_next('a', style="color:#828282;font-size:13px;").text.strip()
        }
        if "ourren" in news_data["title"] or "discuss" in news_data["title"] or "./user/view/" in news_data["link"]:
            continue
        news_list.append(news_data)

    return news_list

def get_saved_ids():
    try:
        with open("news_ids.txt", "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def save_id(news_id):
    with open("sec_wiki_ids.txt", "a") as file:
        file.write(news_id + "\n")

if __name__ == "__main__":
    MAX_RETRIES = 3
    retries=0
    while retries < MAX_RETRIES:
        try:
            news = fetch_news()
            break
        except requests.RequestException as e:
            print(f"Connection attempt {retries + 1} failed. Retrying...")
            retries += 1

    saved_ids = get_saved_ids()
    for item in news:
        if item['id'] not in saved_ids:
            print(f"Date: {item['date']},ID: {item['id']}, Title: {item['title']}, Link: {item['link']}, Author: {item['author']}")
            save_id(item['id'])