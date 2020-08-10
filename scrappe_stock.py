from bs4 import BeautifulSoup
import requests
import time
import csv
from time import localtime, strftime
import matplotlib.pyplot as plt

csv_file = open('YES_BANK_STOCK_PRICES.csv','w')
csv_writer = csv.writer(csv_file)

csv_writer.writerow(['Time Stamp','Stock Prices'])
start_sec = localtime().tm_min*60 + localtime().tm_sec

xdata = []
ydata = []
plt.show()

axes = plt.gca()
axes.set_xlim(0,80)
axes.set_ylim(10,15)
line, = axes.plot(xdata, ydata, 'b-')

def fun():
    url = requests.get('https://finance.yahoo.com/quote/YESBANK.NS?p=YESBANK.NS&.tsrc=fin-srch').text
    soup = BeautifulSoup(url, 'lxml') 
    block = soup.find('div',class_ = 'D(ib) Mend(20px)')

    value = block.find('span').text
    xdata.append((localtime().tm_min*60+localtime().tm_sec) - start_sec)
    ydata.append(float(value))
    line.set_xdata(xdata)
    line.set_ydata(ydata)
    plt.draw()
    csv_writer.writerow([strftime('%Y-%m-%d %H:%M:%S',localtime()),value])
    print('Done Writing'+value)
    plt.pause(1e-17)
    time.sleep(0.1)

for _ in range(60):
    fun()

end_sec =localtime().tm_min*60 + localtime().tm_sec
print(start_sec)
print(end_sec)
print(end_sec-start_sec)
plt.show()
csv_file.close()
