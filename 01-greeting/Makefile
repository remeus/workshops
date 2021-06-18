install:  ## Install virtual environment
	python -m venv ./venv
	. ./venv/bin/activate && pip install -r requirements.txt

test:  ## Run tests
	. ./venv/bin/activate && python -m pytest tests

help:  ## Show help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
