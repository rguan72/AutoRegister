# AutoRegister

A python script to register for classes on Wolverine Access automatically.
UMich classes can fill up really quickly, especially if you have a late registration date. This tool registers for classes for you the moment registration opens.

## Quick Start - Usage

1. Backpack the classes you plan to take on Wolverine Access
2. Run register.py as described [here](#Development)

## Development

```bash
# Clone the repo:
$ git clone https://gitlab.eecs.umich.edu/guanr/autoregister.git

# Make sure you have pip and python3 installed. Also install pipenv:
$ pip install --user pipenv

# Then install all dependencies with pipenv:
$ pipenv install

# Get in virtual environment
$ pipenv shell

# Run script
(AutoRegister) $ python registration.py
```

## License

[MIT](https://github.com/AutoRegister/blob/master/LICENSE)
