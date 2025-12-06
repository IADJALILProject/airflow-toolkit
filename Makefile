# ===========================
# Airflow Toolkit - Makefile
# ===========================

VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
PYTEST = $(VENV)/bin/pytest
RUFF = $(VENV)/bin/ruff
BLACK = $(VENV)/bin/black

# -------- ENVIRONNEMENT --------

venv:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -e ".[dev]"

# -------- QUALITÉ --------

lint:
	$(RUFF) check .

format:
	$(BLACK) .

check-format:
	$(BLACK) --check .

# -------- TESTS --------

test:
	$(PYTEST)

test-unit:
	$(PYTEST) tests/unit/test_date_utils.py tests/unit/test_logging_utils.py tests/unit/test_env_utils.py

test-operators:
	$(PYTEST) tests/operators/test_filesystem_transfer_operator.py tests/operators/test_http_to_filesystem_operator.py

test-integration:
	AIRFLOW__DATABASE__SQL_ALCHEMY_CONN="sqlite:////tmp/airflow_test.db" \
	AIRFLOW__CORE__LOAD_EXAMPLES="False" \
	$(PYTEST) tests/integration/test_dbt_runner_operator.py

# -------- ALL-IN-ONE --------

ci-local: lint check-format test

# -------- CLEAN --------

clean:
	find . -name "__pycache__" -exec rm -rf {} +
	find . -name "*.pyc" -delete
	rm -rf .pytest_cache
	rm -rf $(VENV)
