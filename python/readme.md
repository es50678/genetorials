# Prerequisites
- conda >= 4.9.x

# Set up
- Create your virtual environment.
  - `conda env create -f environment.yml`
- Activate your virtual environment.
  - `conda activate brilliant`
- Install project dependencies (from active virtual environment).
  - `conda install --file requirements.txt`

# Updating dependencies
- `conda list -e > requirements.txt`
