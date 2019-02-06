# python-django-coursemanager

## Overview

Coursemanager is a Django Training Management System:

The system provides the following functionality:

* Maintain a portfolio of courses in a course catalogue.
* Maintain personnel / trainer data.
* Maintain trainer venues and training material.
* Easy to use booking and scheduling of courses.
* Printable trainer diaries and delegate reports.
* Trainer / Training management reports.
* Automate delegate communication.

## Technical Overview

* Developed using Django with lightweight UI based on Admin interface.
* Scalable with various backend databases.
* Customisable, skinnable.

## Status

In development. 

## Setup
``` bash
python -m venv venv
source ./venv/bin/activate

pip install --upgrade pip

pip install django
pip install --upgrade selenium

# TODO: Download the latest gecko driver and copy insto Venv/bin
# (automate) wget https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-linux64.tar.gz
# (automate) | tar -xz > ./venv/bin 

# Create database (SQLite)
python manage.py migrate
python manage.py makemigrations coursemanager
python manage.py sqlmigrate coursemanager 0001
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run Tests
python manage.py test

# Loading Fixtures
python manage.py loaddata

# Dumping dummy users to fixture file
python manage.py dumpdata auth.User --indent 4 > users.json
```