import requests
from bs4 import BeautifulSoup
from datetime import datetime

def AeroPyWx():
    url = 'http://www.aviationweather.gov/adds/tafs/?station_ids=nzch&std_trans=standard&submit_both=Get+TAFs+and+METARs'
    headers = {'user-agent': 'my-app/0.0.1'}
    r = requests.get(url, headers=headers)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")

    strings = []
    for font in soup.findAll('font'):
        strings.append(font.string)

    time = 'Last updated > ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(time)
    print(strings)

AeroPyWx()