#!/bin/bash

cd ./dbs/
sqlite3 crypto <<'END_SQL'
CREATE TABLE IF NOT EXISTS BTC (pricedate timestamp, currency string, rate float);
INSERT INTO BTC ( pricedate, currency, rate ) VALUES (date('now'), 'CUR', 0.0);
DELETE FROM BTC;
END_SQL
ECHO "Database crypto created. Table BTC created. Ready for data insertion."