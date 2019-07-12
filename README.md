# Datos w/ Django: datos-v0b

This project explores [Django](https://www.djangoproject.com/), the python web framework, to create a prototype of the datos website.

## Applications

| Applications  | Description | State |
| ---           | ---         | ---   |
| billing       | Contains everything related to billing such as paypal integration and invoicing | **Active** |
| datasets      | Contains everything about datasets and their download | Soon to be **Inactive** |
| models        | Contains everything about models and their deployment | **Active** |
| services      | Contains the services, action items on a datasets or models, that datos and other users provide, as well as those services a user offers | Inactive |
| subscriptions | Contains the subscriptions of users to a model, dataset | **Active**
| reviews       | Contains reviews about users, models, datasets, services, groups | **Active** |
| tags          | TBD: Should contain everything that should be tagged and searchable | Inactive |
| users         | Contains the extended User class for the datos system | **Active** |

## Requirements
* `pip install django`
* `pip install django-crispy-forms`
* `pip install django-bootstrap4`
* `pip install djangorestframework`

**Note**: It is recommended to use a python environment.

## To run
1. `cd datos-v0b/datos`
2. `python manage.py migrate` - create the database tables for django and datos
3. `python manage.py createsuperuser` - create the admin account
4. `python manage.py runserver` - runs the local server
   1. `python manage.py runserver 0:8000` - to have the server be visible to all LOCAL network devices (e.g. iphone)

**Note**: Any additional `app.models` that are developed need to have their initial migrations generated with this:
1. `python manage.py makemigrations [app_name]`
2. `python manage.py migrate [app_name]`


---

Visit http://127.0.0.1:8000/admin for the administration site. Use login credentials created in step 3.
