import urllib.request
import time
from bs4 import BeautifulSoup
import re

t = time.localtime()
year = str(t.tm_year)
month = str(t.tm_mon).zfill(2)

url = urllib.request.urlopen("http://stu.dje.go.kr/sts_sci_md00_001.do?schulCode=G100000170&schulCrseScCode=4&schulKndScCode=04&schYm="+year+month)
soup = BeautifulSoup(url, 'html.parser')
dsm = soup.find_all('td')
week = []
daily = []
day = []
for a in dsm:
    week.append(str(a).replace('<br/>', '\n').replace('</div></td>',''))
for a in week:
    daily.append(a.split('<td><div>'))
del daily[0:3]
for a in daily :
    day.append(''.join(a).replace('[','SPL[').split('SPL'))


def bab(dayn, meal) :
    if (meal == 0) : return day[dayn][1]+'\n'+day[dayn][2]+'\n'+day[dayn][3]
    else : return day[meal]
