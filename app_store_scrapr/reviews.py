import json
import re
from typing import List, Optional, Any

from app_store_scrapr.utils import requests


def _format(review: dict) -> dict:
    return {
        "id": review["id"]["label"],
        "username": review["author"]["name"]["label"],
        "title": review["title"]["label"],
        "content": review["content"]["label"],
        "version": review["im:version"]["label"],
        "rating": review["im:rating"]["label"],
        "updated": review["updated"]["label"],
    }


def _format_reviews(review_items: List[dict]) -> List[dict]:
    return list(map(_format, review_items))


def _single_page(
    app_id: str, country: str = "us", page: int = 1, sort: str = "mostRecent"
) -> Optional[Any]:
    url = f"https://itunes.apple.com/{country}/rss/customerreviews/page={page}/id={app_id}/sortby={sort}/json"
    data = json.loads(requests.get(url))
    if "feed" in data and "entry" in data["feed"]:
        return data
    return None


def reviews(
    app_id: str, country: str = "us", page: int = 1, sort: str = "mostRecent"
) -> List[dict]:
    entries = _single_page(app_id, country, page, sort)["feed"]["entry"]
    if entries is None:
        return []
    return _format_reviews(entries)


def _get_last_page_number(first_page: dict) -> int:
    for link in first_page["feed"]["link"]:
        if link["attributes"]["rel"] == "last":
            match = re.search(r"page=(\d+)", link["attributes"]["href"])

            if match:
                return int(match.group(1))
            else:
                return 1


def reviews_all(
    app_id: str, country: str = "us", sort: str = "mostRecent"
) -> List[dict]:
    first_page = _single_page(app_id, country, 1, sort)
    if first_page is None:
        return []

    last_page_number = _get_last_page_number(first_page) + 1
    reviews_array = _format_reviews(first_page["feed"]["entry"])

    for cur_page_number in range(2, last_page_number):
        cur_page = _single_page(app_id, country, cur_page_number, sort)
        if cur_page is None:
            break
        reviews_array += _format_reviews(cur_page["feed"]["entry"])

    return reviews_array
