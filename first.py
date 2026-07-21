import requests
from requests_cache import CachedSession
from datetime import datetime, timedelta
from ratelimit import limits, sleep_and_retry

now = datetime.now()
midnight = (now + timedelta(days=1)).replace(
    hour=0, minute=0, second=0, microsecond=0
)
till_midnight = midnight - now
session = CachedSession('cache', expire_after=till_midnight, use_cache_dir=True)
result = []


class Parser:
    def __init__(self, result, session):
        self.result = result
        self.session = session

    @limits(calls=15, period=900)
    @sleep_and_retry
    def resp(self):
        try:
            url_d = "https://api.nbrb.by/exrates/rates?periodicity=0"
            url_m = "https://api.nbrb.by/exrates/rates?periodicity=1"
            combined = []
            resp_d = self.session.get(url_d)
            resp_d.raise_for_status()
            resp_m = self.session.get(url_m)
            resp_m.raise_for_status()
            combined = resp_d.json() + resp_m.json()
            for i in combined:
                self.result.append(i['Cur_Abbreviation'])
                self.result.append(i['Cur_Name'])
                self.result.append(i['Cur_OfficialRate'])
        except requests.exceptions.ConnectionError:
            print('Connection error')
        except requests.exceptions.HTTPError:
            print('HTTP error')
        except requests.exceptions.RequestException:
            print('Request error')
        except requests.exceptions.ReadTimeout:
            print('Request timed out')

    #error handling

    def file_creator(self):
        with open('cur_today.csv', 'w', encoding="utf-8-sig", newline="") as file:
            for idx, i in enumerate(self.result, start=1):
                file.write(str(i))
                file.write('\n' if idx % 3 == 0 else ' ')


p = Parser(result, session)
print(p.resp())
print(p.file_creator())