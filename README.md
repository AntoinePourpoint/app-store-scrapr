
# app-store-scrapr

[![Black Code Style](https://img.shields.io/badge/code%20style-black-100000.svg)](https://github.com/python/black)
[![PyPI](https://img.shields.io/pypi/v/app-store-scrapr.svg)](https://pypi.org/project/app-store-scrapr/)

`app-store-scrapr` is a Python library for scraping reviews from the Apple App Store. It provides an easy-to-use interface to gather reviews for iOS apps.

## Features

- **Get Specific Page Reviews**: Retrieve reviews from a specific page for an app.
- **Get All Reviews**: Conveniently fetch reviews from all available pages (up to 10 pages).

## Requirements

- Python 3.8 or higher

## Installation

Install `app-store-scrapr` using pip:

```bash
pip install app-store-scrapr
```

## Usage

### Getting Reviews from a Specific Page

To get reviews from a specific page for an app, use the `reviews` method:

```python
from app_store_scrapr.reviews import reviews

# Parameters:
# app_id (str): The app's unique identifier.
# country (str, optional): The country code (default is 'us').
# page (int, optional): The page number to retrieve (default is 1).
# sort (str, optional): The sort order, 'mostRecent' or 'mostHelpful' (default is 'mostRecent').

app_reviews = reviews(app_id='123456789', country='us', page=3, sort='mostRecent')
print(app_reviews)
```

### Getting All Reviews

To get all reviews (up to 10 pages) for an app, use the `reviews_all` method:

```python
from app_store_scrapr.reviews import reviews_all

# Parameters:
# app_id (str): The app's unique identifier.
# country (str, optional): The country code (default is 'us').
# sort (str, optional): The sort order, 'mostRecent' or 'mostHelpful' (default is 'mostRecent').

all_reviews = reviews_all(app_id='123456789', country='us', sort='mostRecent')
print(all_reviews)
```

## Contributing

Contributions to `app-store-scrapr` are welcome! If you have an idea or suggestion, please:

1. Open an issue to discuss what you would like to change or add.
2. Once the proposal is discussed and approved, you can fork the repository and create a pull request.

## License

`app-store-scrapr` is MIT licensed. See the [LICENSE](LICENSE) file for more details.
