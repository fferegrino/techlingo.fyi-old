clean:
	rm -rf output content/generated

build:
	PYTHONPATH=. python tech/transform.py
	pelican content -t themes/simple -s publishconf.py

fmt:
	PYTHONPATH=. python tech/format.py

run: build
	pelican --listen
