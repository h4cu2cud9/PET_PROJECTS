import requests

url_d = "https://api.nbrb.by/exrates/rates?periodicity=0"
url_m = "https://api.nbrb.by/exrates/rates?periodicity=1"
resp_d = requests.get(url_d)
resp_m = requests.get(url_m)
data_d = resp_d.json()
data_m = resp_m.json()

for i in data_d:
    print(i['Cur_Name'], i['Cur_OfficialRate'])

print('\n')

for j in data_m:
    print(j.get('Cur_Name'), j.get('Cur_OfficialRate'))
#parent class
'Cur_Abbreviation'
'Cur_QuotName'
...


#child class


