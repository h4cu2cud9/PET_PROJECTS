import requests

url_d = "https://api.nbrb.by/exrates/rates?periodicity=0"
url_m = "https://api.nbrb.by/exrates/rates?periodicity=1"
result = []

class Parser:
    def __init__(self, url_d, url_m, result):
        self.url_d = url_d
        self.url_m = url_m
        self.result = result

    def resp(self):
        try:
            combined = []
            resp_d = requests.get(self.url_d)
            resp_d.raise_for_status()
            resp_m = requests.get(self.url_m)
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


p = Parser(url_d, url_m, result)
print(p.resp())
print(p.file_creator())