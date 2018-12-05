## AutoRegister

This is an application for automatically registering for Winter 2019 UMich classes.

## Preparation - Usage

To prepare for auto register to work, backpack the classes you plan to take.

## Running

(before exe)
Get in the virtual environment:
`$ pipenv shell`

Run the python script in terminal
`(virtualenv)$ python registration.py`
Select "Run Later" if you want the script to wait for your registration date to run. Select "Run Now" if you want the script to register for your classes now. You will be prompted to enter your umich uniqname and password.

## TODO

Create an .exe (or equivalent for mac) executable.

## Development
Clone the repo:
`git clone https://gitlab.eecs.umich.edu/guanr/autoregister.git`

Make sure you have pip and python3 installed. Also install pipenv:
`$ pip install --user pipenv`

Then install all dependencies with pipenv:
`$ pipenv install`

Clone the repo and run
`$ pipenv shell`.
From there, you are ready to contribute!

## WARNING -- NEED TO FIX
If the chromedriver window is closed, everything breaks!

## Authors
* **Richard Guan**
