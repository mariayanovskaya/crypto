from btcscrape import scrape
from datetime import datetime


def test_scrape():
    date, currency, rate = scrape('USD')
    assert date.date() == datetime.now().date()
    assert currency == 'USD'
    assert isinstance(rate, float) is True