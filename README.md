## Virtual Env (W,Windows),(L,Linux),(M,Mac)

#### Create virtual environment (W,L)
* virtualenv: `virtualenv <envName>`
* python3 venv: `python3 -m venv <envName>`

#### Windows Security Authorization (W)
* `Set-ExecutionPolicy Unrestricted -Scope Process`

#### Start virtual environment 
* (W): `.\\<patchEnv>\<envName>\Scripts\activate`
* (L): `source <patchEnv>/<envName>/bin/activate`

#### Stop virtual environment (W,L)
* `deactivate`

## Djando

#### Create Project
* `django-admin startproject <projectName>`

#### Create App
* `python manage.py startapp <appName>`

#### Install App
* open Settings.py and add you `<appName>` to list `INSTALLED_APPS`

#### Migrate
* `python manage.py migrate`

#### Run Server
* `python manage.py runserver`

