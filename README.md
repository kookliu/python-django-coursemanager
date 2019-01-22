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

# Update pip 
pip install django

# Create database (SQLite)
python manage.py migrate
python manage.py makemigrations coursemanager
python manage.py sqlmigrate coursemanager 0001
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```