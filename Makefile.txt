.PHONY: tests clean

setup:
	uv venv env
	- env/bin/activate
	uv pip install -r requirements.txt

test:
	source: .venv/bin/activate
	pytest test_dataset.py