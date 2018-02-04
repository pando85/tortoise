VENV_BASE += .venv
VENV_BIN := $(VENV_BASE)/bin
PROJECT := tortoise

.PHONY: venv requirements requirements_dev pep8 falke8 check clean

venv:
	if [ ! -d "$(VENV_BASE)" ]; then \
		virtualenv -p python3 $(VENV_BASE); \
	fi

requirements: venv
	${VENV_BIN}/pip install -r requirements.txt

requirements_dev: requirements
	${VENV_BIN}/pip install -r requirements_dev.txt

pycodestyle: requirements_dev
	${VENV_BIN}/$@ tortoise_bot

flake8: requirements_dev
	${VENV_BIN}/$@ tortoise_bot

check: pycodestyle flake8

clean:
	rm -rf $(VENV_BASE)
