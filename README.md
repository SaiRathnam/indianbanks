# indianbanks

## API 1: given an ifsc_code, get branch details
URL:https://indianbanksserver.herokuapp.com/v1/banks/branches/{ifsc_code}

Query params: ifsc_code

## API 2: given a bank name and a city, get all branches
URL:https://indianbanksserver.herokuapp.com/v1/banks/all_branches

Query params: bank_name, city

Note: Only first 9000 rows from the branches table have been copied over to the heroku postgres instance.

Sample input for API 2:

`bank_name = ABHYUDAYA COOPERATIVE BANK LIMITED`

`city = MUMBAI`

## Setting up app on local

`python 3.x`

1. Create a virtual environment

`$ virtualenv venv`

2. Pip install all the requirements

`$ pip install -r requirements.txt`

3. Setup the local database

4. Copy over contents from `envs_template.sh` into `envs.sh` and export all necessary environment variable values

`$ source envs.sh`

5. Start the app (in development mode)

`$ python3 app.py`
