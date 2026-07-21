import pytest
import first
import csv
from requests_cache import CachedSession
from datetime import datetime, timedelta


now = datetime.now()
midnight = (now + timedelta(days=1)).replace(
    hour=0, minute=0, second=0, microsecond=0
)
till_midnight = midnight - now


parser = first.Parser(result=[], session=CachedSession('cache', expire_after=till_midnight, use_cache_dir=True))
result = parser.file_creator()

def test_file():
    with open('cur_today.csv', newline='') as f:
        file = csv.reader(f)
    assert pytest.raises(FileNotFoundError)







