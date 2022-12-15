install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C btcscrape

test:
	pytest -q

format:
	black *.py