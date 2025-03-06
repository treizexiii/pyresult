# Variables
PACKAGE_NAME = pyresult
ifeq ($(OS),Windows_NT)
	PYTHON = python
else
	PYTHON = python3
endif
PIP = pip
PYTEST = pytest
TWINE = twine

ifeq ($(OS),Windows_NT)
    SET_ENV = set PYTHONPATH=src &&
else
    SET_ENV = PYTHONPATH=src
endif

ifeq ($(OS),Windows_NT)
	RM = rm .venv && rm build && rm dist && rm *.egg-info && rm __pycache__
else
	RM = rm -rf .venv build dist *.egg-info __pycache__
endif

setup:
	$(PYTHON) -m venv .venv
	. .venv/bin/activate

# 📦 Installation des dépendances
install:
	$(PIP) install -r requirements.txt

# 🔨 Build du package
build:
	$(PYTHON) -m build

# 🚀 Installation du package localement
install-package:
	$(PIP) install .

# 🧪 Lancer les tests avec pytest et coverage
test:
	$(SET_ENV) $(PYTEST) --cov=$(PACKAGE_NAME) --cov-report=term-missing

# 📊 Générer un rapport HTML de couverture
coverage:
	$(SET_ENV) $(PYTEST) --cov=$(PACKAGE_NAME) --cov-report=html
	@echo "Ouvrir le rapport avec : xdg-open htmlcov/index.html"

# 📤 Publier le package sur PyPI
publish:
	$(TWINE) upload dist/*

# 🧹 Nettoyage des fichiers générés
clean:
	rm -rf build dist *.egg-info __pycache__
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete

# 🏁 Tout exécuter : build, test, coverage
all: clean build test coverage