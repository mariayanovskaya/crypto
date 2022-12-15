install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C btcscrape

test:
	pytest -vv --cov-report term-missing --cov=btcscrape test_*.py

format:
	black *.py