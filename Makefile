NAME = a_maze_ing

VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

FLAKE8 = $(VENV)/bin/flake8
MYPY = $(VENV)/bin/mypy

MYPY_FLAGS = --warn-return-any --warn-unused-configs

install:
	@if [ ! -d "$(VENV)" ]; then \
		python3 -m venv $(VENV); \
	fi
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) $(NAME).py

debug:
	$(PYTHON) -m pdb $(NAME).py

lint:
	$(FLAKE8) .
	$(MYPY) $(MYPY_FLAGS) .

lint-strict:
	$(FLAKE8) .
	$(MYPY) --strict .

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

fclean: clean
	rm -rf $(VENV)

.PHONY: install run debug lint lint-strict clean fclean
