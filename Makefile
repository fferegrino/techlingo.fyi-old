clean:
	rm -rf output content/generated

build:
	PYTHONPATH=. python tech/transform.py
	pelican content -t themes/simple -s publishconf.py

lint:
	black . --check
	isort . --check-only

fmt:
	black .
	isort .
	PYTHONPATH=. python tech/format.py

run: build
	pelican --listen
