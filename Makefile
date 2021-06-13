clean:
	rm -rf output content/generated

build:
	PYTHONPATH=. python tech/transform.py
	pelican content

fmt:
	PYTHONPATH=. python tech/format.py

run: build
	pelican --listen
