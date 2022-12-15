import btcscrape

if __name__ == '__main__':

    wrong_dir = True
    while :
        btcscrape.write_to_db(btcscrape.scrape())
        time.sleep(60)