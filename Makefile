# Variables
PACKAGE_NAME = pyresult
PYTHON = python
PIP = pip
PYTEST = pytest
TWINE = twine

ifeq ($(OS),Windows_NT)
    SET_ENV = set PYTHONPATH=src &&
else
    SET_ENV = PYTHONPATH=src
endif

# 📦 Installation des dépendances
install:
	$(PIP) install -r requirements.txt

# 🔨 Build du package
build:
	$(PYTHON) setup.py sdist bdist_wheel

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