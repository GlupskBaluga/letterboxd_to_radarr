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
python3 movies_by_user_and_rating.py <username> <min_rating> <max_rating> [<out_path>] [--direct]
```
#### Default (creates "added_movies_by_<user>" in current directory)
```bash
python3 movies_by_user_and_rating.py someuser 3 5
```
#### With custom output path
```bash
python3 movies_by_user_and_rating.py someuser 3 5 /path/to/output
```
#### Direct mode (movie folders created directly in output path)
```bash
python3 movies_by_user_and_rating.py someuser 3 5 /path/to/output --direct
```
### Import movies from a user's watchlist
```bash
python3 watchlist_by_user.py <username> [<out_path>] [--direct]
```
#### Default (creates "watchlist_by_<user>" in current directory)
```bash
python3 watchlist_by_user.py filmtonsen
```
#### With custom output path
```bash
python3 watchlist_by_user.py filmtonsen /path/to/output
```
#### Direct mode
```bash
python3 watchlist_by_user.py filmtonsen /path/to/output --direct
```
Now that the folders are made, Radarr automatically finds these entries and they can be mass-imported/downloaded. 

> This project is for educational purposes only.  
> Use at your own risk.
