NAME = a_maze_ing

VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

FLAKE8 = $(VENV)/bin/flake8
MYPY = $(VENV)/bin/mypy

FLAKE8_EXCLUDE = .git,__pycache__,$(VENV)
MYPY_EXCLUDE = ^$(VENV)/

MYPY_FLAGS = --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

install:
	@if [ ! -d "$(VENV)" ]; then \
		python3 -m venv $(VENV); \
	fi
	$(PIP) install -r requirements.txt

shell: install
	@echo "Shell with $(VENV) active. Type 'exit' to leave."
	@. $(VENV)/bin/activate && exec $${SHELL:-/bin/bash} -i

run:
	$(PYTHON) $(NAME).py config.txt

debug:
	$(PYTHON) -m pdb $(NAME).py

lint:
	$(FLAKE8) --exclude $(FLAKE8_EXCLUDE) .
	$(MYPY) $(MYPY_FLAGS) --exclude '$(MYPY_EXCLUDE)' .

lint-strict:
	$(FLAKE8) --exclude $(FLAKE8_EXCLUDE) .
	$(MYPY) --strict --exclude '$(MYPY_EXCLUDE)' .

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

fclean: clean
	rm -rf $(VENV)

.PHONY: install shell run debug lint lint-strict clean fclean
