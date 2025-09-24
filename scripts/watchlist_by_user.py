import sys
from bs4 import BeautifulSoup
import requests
import os

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 watchlist_by_user.py <username>")
        sys.exit(1)
    else:
        print("Usage: python3 watchlist_by_user.py <username>")

    # block avoidance
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
                    " AppleWebKit/537.36 (KHTML, like Gecko)"
                    " Chrome/140.0.0.0 Safari/537.36"
    })

    user = sys.argv[1]

    # more settings
    out_path = os.getcwd()
    direct = False          # --direct makes the script create the movie folders directly in the selected path
    if len(sys.argv) >= 3 and sys.argv[2] != "--direct":
        out_path = sys.argv[2]
    if "--direct" in sys.argv[2:]:
        direct = True

    url = f'https://letterboxd.com/{user}/watchlist/'

    pages = len(BeautifulSoup(session.get(url).text, 'html.parser').find_all(class_="paginate-page"))

    movies = []

    for page in range(pages):
        page_url = f'{url}/page/{page+1}/'
        page_doc = BeautifulSoup(session.get(page_url).text, 'html.parser')
        print(page_doc)
        items = page_doc.find(class_="grid -p125 -scaled128").find_all(class_="griditem")
        movies += [item.div["data-item-full-display-name"] for item in items]

    if direct:
        base_dir = out_path
    else:
        base_dir = os.path.join(out_path, f'watchlist_by_{user}')
        try:
            os.mkdir(base_dir)
        except FileExistsError:
            print("User Folder already exists")

    created = 0
    skipped = 0

    for movie in movies:
        try:
            os.mkdir(os.path.join(base_dir, movie.replace(":", "")))
            created += 1
        except FileExistsError:
            print("Directory already exists")
            skipped += 1
            
    # final status
    print(f"\nDone. Found {len(movies)} movies in watchlist.")
    print(f"Created {created} new folders, skipped {skipped} (already existed).")
    print(f"Output path: {base_dir}")