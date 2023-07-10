# Bike-Fitting-Application

## Introduction
This application is being created as part of a semester project.<br>
You can creat your own fitting vor different bike types.<br>

For more technical stuff checkout our [developer manual](https://github.com/lukaskonietzka/bikefitting/blob/main/DeveloperManualGerman.pdf).<br>

## Usage
To use the App in the developer mode, follow the Steps below:

1. Clone the repository 
2. Change in the Projekt folder
3. Install all required packages via _requirements.txt_ or manual
4. synchronize the database with _python manage.py --run-syncdb_
5. Create a superuser with: _python manage.py createsuperuser_ to get full access to all pages
3. Type _python manage.py runserver_ to start the developer server
4. Click on the localhost link.
5. Now you can use the App
6. To manage the database type _/admin_ into the url-path.

>Important: If you use the App in a running system, set the debug mode to _False_.

## Collaborators
- __Sebastian Niehage__
- __Lukas Konietzka__

## Framework
For our app we use Django as framework.
For more information about the Django framework checkout the [Dokumentation](https://www.djangoproject.com/)

## Tests
We use unittest to test our software.
To run the tests follow the steps below:
1. Change into the folder /bikefitting_app/tests with: _cd /bikefitting_app/tests_
2. Type in _pytest_ to run all test in this folder
