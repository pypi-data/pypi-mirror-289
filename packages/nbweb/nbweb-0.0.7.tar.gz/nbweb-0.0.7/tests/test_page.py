import pytest

from nbweb.page import Page

url_filename = [
    [
        "https://odishatv.in/news/weather/17-places-in-odisha-receive-very-heavy-rain-banki-records-highest-317-mm-rainfall-in-past-24-hours-241035",
        "odishatv_in_news_weather_17_places_in_odisha_receive_very_heavy_rain_banki_records_highest_317_mm_rainfall_in_past_24_hours_241035",
    ],
    [
        "https://www.techspot.com/news/104151-old-school-mainframes-could-see-renewed-life-ai.html",
        "www_techspot_com_news_104151_old_school_mainframes_could_see_renewed_life_ai_html",
    ],
    ["https://dummy.site.com/all/-in-title#main", "dummy_site_com_all_in_title"],
    [
        "https://sample.abc.com/news/with-filter?main=scale",
        "sample_abc_com_news_with_filter",
    ],
]


@pytest.mark.parametrize("url,filename", url_filename)
def test_filename(url: str, filename: str) -> None:
    p = Page(url)
    assert p.filename == filename


def test_failure() -> None:
    url = "https://subratlima.xyz"
    p = Page(url)
    html = p.get()
    assert html is None


def test_success() -> None:
    url = "https://httpbin.org"
    p = Page(url)
    html = p.get()
    assert html is not None


def monkeypatch_func(*kargs, **kwargs) -> None:
    return "one two three"


def test_load_from_cache(monkeypatch) -> None:
    url = "https://httpbin.org/get"
    p = Page(url)
    html = p.get()
    assert html is not None
    assert html != "one two three"

    monkeypatch.setattr(Page, "_fetch_from_cache", monkeypatch_func)
    p2 = Page(url)
    html = p2.get()

    assert html == "one two three"
