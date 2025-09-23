# letterboxd_to_radarr
A small script for quickly importing movies from **Letterboxd** to **Radarr**. 

## Requirements
Install dependencies with:
```bash
pip install beautifulsoup4 requests
```

## Usage:
### Import movies by user and rating
```bash
python3 movies_by_user_and_rating.py <username> <min_rating> <max_rating>
```
Example:
```bash
python3 movies_by_user_and_rating.py someuser 3 5
```

### Import movies from a user's watchlist
```bash
python3 watchlist_by_user.py <username>
```
Example:
```bash
python3 watchlist_by_user.py filmtonsen
```
