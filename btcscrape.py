from urllib import request
import json
from datetime import datetime
import sqlite3
import os
import sys
import time

def main():
    '''my btc scrape'''



    url = f'https://api.coindesk.com/v1/bpi/currentprice/GBP.json'
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

    req = request.Request(url, headers = header)
    with request.urlopen(req) as data:
        jdata = json.load(data)

    dt = datetime.strptime(jdata['time']['updateduk'], '%b %d, %Y at %H:%M %Z')
    rate = jdata['bpi']['GBP']['rate_float']

    # change dir if you are not in db dir
    global wrong_dir
    if wrong_dir:
        os.chdir('./dbs/')
        wrong_dir = False
    conn = sqlite3.connect('crypto')
    c = conn.cursor()
    #c.execute("SELECT * FROM table_name ")
    #print(c.fetchall())
    param = (dt, 'GBP', rate)
    try:
        c.execute('insert into BTC ( pricedate, currency, rate ) values (?, ?, ?)', param)
    except Exception as e: # TODO: this is a mess, get proper exception handelling
        print(e)
        print('could not insert, exiting')
        sys.exit()

    conn.commit()
    conn.close()


if __name__ == '__main__':

    wrong_dir = True
    while True:
        main()
        time.sleep(60)


