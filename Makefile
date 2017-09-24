VENV_BIN := .venv/bin

.venv:
	virtualenv -p python3 .venv
	${VENV_BIN}/pip install -r requirements.txt

check_requirements:
	@${VENV_BIN}/pip freeze > freeze.txt
	@diff requirements.txt freeze.txt > /dev/null 2>&1 || ${VENV_BIN}/pip install -r requirements.txt
	@rm freeze.txt

run: .venv check_requirements
	${VENV_BIN}/python manage.py runserver

test: .venv
	${VENV_BIN}/python manage.py test
	
clean:
	rm -rf .venv

.PHONY: run check_requirements
