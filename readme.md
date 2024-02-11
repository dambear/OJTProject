# Project Name

## Overview

Briefly describe your project and its purpose.

## Prerequisites

- Python 3.x installed
- [Optionally, any other dependencies]

how to run in 

## Setting up Python Virtual Environment

### Create Virtual Environment

To create a Python virtual environment, open a terminal and run the following command:

```bash
python -m venv ./ilcdbcore-env


./ilcdbcore-env/Scripts/activate

```

## Setting up New Database Reminder

### in model.py comment the comment i make also in setting.py

run this first

```bash
python manage.py makemigrations

python manage.py migrate
```

run this code after you migrate
this code is for the user custom table to be generated

```bash
python manage.py migrate --run-syncdb

```

create user admin

```bash

python manage.py createsuperuser     

```
