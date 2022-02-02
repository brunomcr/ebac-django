# ebac-django
# Django

## Virtual Env (Windows)

#### Create virtual environment
* `virtualemv <envName>`

#### Windows Security Authorization
* `Set-ExecutionPolicy Unrestricted -Scope Process`

#### Start virtual environment
* `.\\<patchEnv>\<envName>\Scripts\activate`

#### Stop virtual environment
* `deactivate`

## Djando Setup

#### Create Project
* `django-admin startproject <projectName>`

#### Create App
* go to you project folder `cd <patchProject>\<projectName>`
* * `python manage.py startapp <appName>`

#### Install App
* open Settings.py and add you `<appName>` to list `INSTALLED_APPS`

#### Migrate
* `python manage.py migrate`

#### Run Server
* `python manage.py runserver`

