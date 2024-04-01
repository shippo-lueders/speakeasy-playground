init-venv:
	if [ ! -d ".venv" ]; then python3 -m venv .venv; fi

install: init-venv
	source .venv/bin/activate; python3 -m pip install .[dev]

generate:
	speakeasy generate sdk -s openapi.yaml -o . -l python
