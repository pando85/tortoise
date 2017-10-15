VENV_BASE += .venv
VENV_BIN := $(VENV_BASE)/bin
PROJECT := tortoise

.PHONY: venv requirements requirements_dev makemigrations migrate run \
		test reports pep8 falke8 check clean

venv:
	virtualenv -p python3 $(VENV_BASE)

requirements: venv
	${VENV_BIN}/pip install -r requirements.txt

requirements_dev: requirements
	${VENV_BIN}/pip install -r requirements_dev.txt

makemigrations:
	${VENV_BIN}/python manage.py makemigrations

migrate:
	${VENV_BIN}/python manage.py migrate

run: venv requirements makemigrations migrate
	${VENV_BIN}/python manage.py runserver

test: venv
	${VENV_BIN}/python manage.py test

reports:
	mkdir -p $@

pep8: requirements_dev reports
	@(set -o pipefail && $@ | tee reports/$@.report)

flake8: requirements_dev reports
	@(set -o pipefail && $@ | tee reports/$@.report)

check: pep8 flake8

clean:
	rm -rf $(VENV_BASE)
