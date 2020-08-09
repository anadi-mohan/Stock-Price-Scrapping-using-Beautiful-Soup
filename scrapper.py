import time
from bs4 import BeautifulSoup
import requests
import csv
source = requests.get('https://finance.yahoo.com/trending-tickers').text
soup = BeautifulSoup(source , 'lxml')
csv_file = open('Stock_prices.csv','w')
csv_writer = csv.writer(csv_file)

def fun():
    source = requests.get('https://finance.yahoo.com/trending-tickers').text
    soup = BeautifulSoup(source , 'lxml')
    values = soup.findAll('td', class_='data-col2 Ta(end) Pstart(20px)')
    csv_writer.writerow([i.text for i in values])
    print('Done Writing')
    time.sleep(5)

names = soup.findAll('td', class_='data-col1 Ta(start) Pstart(10px) Miw(180px)')
csv_writer.writerow([i.text for i in names])

for _ in range (720):
    fun()

csv_file.close()
