def main():
    '''my btc scrape'''

    from urllib import request
    import json
    from datetime import datetime
    import sqlite3

    url = f'https://api.coindesk.com/v1/bpi/currentprice/GBP.json'
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

    req = request.Request(url, headers = header)
    with request.urlopen(req) as data:
        jdata = json.load(data)

    dt = datetime.strptime(jdata['time']['updateduk'], '%b %d, %Y at %H:%M BST')
    rate = jdata['bpi']['GBP']['rate_float']
    conn = sqlite3.connect(r'C:\projects\crypto\dbs\crypto')
    c = conn.cursor()
    param = (dt, 'GBP', rate)
    c.execute('insert into BTC ( pricedata, currency, rate ) values (?, ?, ?)', param)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    import time
    while True:
        main()
        time.sleep(60)

