
import sys
from bs4 import BeautifulSoup
import requests
import os

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 movies_by_user_and_rating.py <username> <min_rating> <max_rating>")
        sys.exit(1)
    else:
        print("Usage: python3 movies_by_user_and_rating.py <username> <min_rating> <max_rating>")

    # block avoidance
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
                    " AppleWebKit/537.36 (KHTML, like Gecko)"
                    " Chrome/140.0.0.0 Safari/537.36"
    })

    user = sys.argv[1]
    min_rating = sys.argv[2]
    max_rating = sys.argv[3]

    rating = f"{min_rating}-{max_rating}"
    url = f'https://letterboxd.com/{user}/films/rated/{rating}/'

    pages = len(BeautifulSoup(session.get(url).text, 'html.parser').find_all(class_="paginate-page"))

    movies = []

    for page in range(pages):
        page_url = f'{url}/page/{page+1}/'
        page_doc = BeautifulSoup(session.get(page_url).text, 'html.parser')
        print(page_doc)
        items = page_doc.find(class_="grid -p70").find_all(class_="griditem")
        movies += [item.div["data-item-full-display-name"] for item in items]

    try:
        os.mkdir(f'added_movies_by_{user}')
    except FileExistsError:
        print("User Folder already exists") 

    for movie in movies:
        try:
            os.mkdir(f'added_movies_by_{user}/{movie.replace(":", "")}')
        except FileExistsError:
            print("Directory already exists")


