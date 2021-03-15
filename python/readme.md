# Prerequisites
- python 3.8.7 and `virtualenv`
  - `pip install virtualenv`

# Set up
- Create your virtual environment.
  - `python -m virtualenv --prompt '(tourmaline-content) ' ./venv/main`
- Activate your virtual environment.
  - `source ./venv/main/bin/activate`
- Install project dependencies (from active virtual environment).
  - `pip install -r ./requirements.txt`

# Updating dependencies
- `pip freeze > requirements.txt`
