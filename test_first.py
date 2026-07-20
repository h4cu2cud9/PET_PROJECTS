import pytest
import first
import csv


parser = first.Parser(url_d="https://api.nbrb.by/exrates/rates?periodicity=0", url_m="https://api.nbrb.by/exrates/rates?periodicity=1", result=[])
result = parser.file_creator()

def test_file():
    with open('cur_today.csv', newline='') as f:
        file = csv.reader(f)
    assert pytest.raises(FileNotFoundError)







