# Datos w/ Django: datos-v0b

This project explores [Django](https://www.djangoproject.com/), the python web framework, to create a prototype of the datos website.

## Applications

| Applications  | Description |
| ---           | ---         |
| homepage      | Contains the homepage |
| datasets      | Contains everything about datasets and their download |
| models        | Contains everything about models and their deployment |
| services      | Contains the services, action items on a datasets or models, that datos and other users provide, as well as those services a user offers |
| subscriptions | Contains the subscriptions of users to a model, dataset |
| reviews       | Contains reviews about users, models, datasets, services, groups |

## Requirements
* `pip install django`
* `pip install django-crispy-forms`
* `pip install django-bootstrap4`

**Note**: It is recommended to use a python environment.

## To run
1. `cd datos-v0b/`
2. `python manage.py migrate`
3. `python manage.py createsuperuser`
4. `python manage.py runserver`

**Note**: Any additional `app.models` that are developed need to have their initial migrations generated with this:

`python manage.py makemigrations [app_name]`
