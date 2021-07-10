clean:
	rm -rf output content/generated

build:
	PYTHONPATH=. python -m tech convert
	pelican content -t themes/simple -s publishconf.py

tweet:
	PYTHONPATH=. python -m tech tweet

lint:
	black . --check
	isort . --check-only

fmt:
	black .
	isort .
	PYTHONPATH=. python tech/format.py

run: build
	pelican --listen
