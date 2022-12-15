from urllib import request
import json
from datetime import datetime
import sqlite3
import os
import sys
import time
import click



def scrape(currency='GBP'):
    '''The function that scrapes the bitcoin price for a specified currency'''

    url = f'https://api.coindesk.com/v1/bpi/currentprice/{currency}.json'
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

    req = request.Request(url, headers = header)
    with request.urlopen(req) as data:
        if data.status != 200:
            raise ConnectionError
        jdata = json.load(data)
    
    dt = datetime.strptime(jdata['time']['updateduk'], '%b %d, %Y at %H:%M %Z')
    rate = jdata['bpi'][currency]['rate_float']

    return dt, currency, rate

@click.command()
@click.option(
    "--pricedate",
    prompt="Timestamp for the price: ",
    help="Provides and exact timestamp for the bitcoin price",
)
@click.option(
    "--currency",
    prompt="Currency: ",
    help="The 3 letter code of the currency to be scraped for the price of bitcoin, i.e. GBP (default)",
)
@click.option(
    "--rate",
    prompt="Rate: ",
    help="The bitcoin price.",
)
def write_to_db(pricedate, currency, rate):
    '''A function that writes the datetime, currency and the price of bitcoin to the sqlite db'''
    global wrong_dir
    if wrong_dir:
        os.chdir('./dbs/')
        wrong_dir = False
    conn = sqlite3.connect('crypto')
    c = conn.cursor()
    #c.execute("SELECT * FROM table_name ")
    #print(c.fetchall())
    param = (pricedate, currency, rate)

    c.execute('insert into BTC ( pricedate, currency, rate ) values (?, ?, ?)', param)

    conn.commit()
    conn.close()
    return

