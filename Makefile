clean:
	rm -rf output content/generated

build:
	PYTHONPATH=. python tech/transform.py
	pelican content

run: build
	pelican --listen
