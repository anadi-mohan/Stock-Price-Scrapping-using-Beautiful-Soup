from bs4 import BeautifulSoup
import requests
import time
import csv
from time import localtime, strftime

csv_file = open('YES_BANK_STOCK_PRICES.csv','w')
csv_writer = csv.writer(csv_file)

csv_writer.writerow(['Time Stamp','Stock Prices'])
start_sec = localtime().tm_min*60 + localtime().tm_sec
def fun():
    url = requests.get('https://finance.yahoo.com/quote/YESBANK.NS?p=YESBANK.NS&.tsrc=fin-srch').text
    soup = BeautifulSoup(url, 'lxml') 
    block = soup.find('div',class_ = 'D(ib) Mend(20px)')

    value = block.find('span').text
    csv_writer.writerow([strftime('%Y-%m-%d %H:%M:%S',localtime()),value])
    print('Done Writing'+value)
    time.sleep(0.1)

for _ in range(60):
    fun()

print((localtime().tm_min*60 + localtime().tm_sec)-start_sec)
csv_file.close()
