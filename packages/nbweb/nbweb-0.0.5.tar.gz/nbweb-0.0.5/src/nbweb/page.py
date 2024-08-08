import os
import re

from datetime import datetime
from datetime import timedelta

import httpx

from fake_useragent import UserAgent


HOME_DIR = os.path.expanduser("~")
HTML_DIR = os.path.join(HOME_DIR, ".cache", "nbweb", "html")
CACHE_SAVE_DAYS = 1


class Page:
    def __init__(self, url: str) -> None:
        self.url = url
        self._set_folder()
        self._set_filename()
        self._clear_old_cache()

    def get(self) -> str:
        if os.path.exists(self.filepath):
            html = self._fetch_from_cache()
        else:
            html = self._fetch()
            if html is not None:
                self._save_to_cache(html)
        return html

    def _set_folder(self) -> None:
        if not os.path.exists(HTML_DIR):
            os.makedirs(HTML_DIR)

    def _clear_old_cache(self):
        cache_expiry_date = datetime.today() - timedelta(days=CACHE_SAVE_DAYS)
        for filename in os.listdir(HTML_DIR):
            filepath = os.path.join(HTML_DIR, filename)
            creation_ts = os.path.getctime(filepath)
            if creation_ts < cache_expiry_date.timestamp():
                os.remove(filepath)

    def _set_filename(self) -> None:
        regex = r"^(https?://)?(?P<url>[^?#]+)"
        result = re.search(regex, self.url)
        self.filename = re.sub(r"\W+", "_", result.group("url"))
        self.filepath = os.path.join(HTML_DIR, self.filename)

    def _fetch(self) -> str:
        try:
            ua = UserAgent(platforms="pc")
            headers = {"User-Agent": ua.random}
            r = httpx.get(self.url, headers=headers)
            r.raise_for_status()
        except httpx.HTTPError:
            print("could not fetch page")
            return None
        return r.text

    def _fetch_from_cache(self) -> str:
        with open(self.filepath) as f:
            html = f.read()
        return html

    def _save_to_cache(self, html):
        with open(self.filepath, "w") as f:
            f.write(html)
