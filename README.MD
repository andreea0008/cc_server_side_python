# Guide

### Base requirements
python 3.6


### Set up enviroment. Run project
- create project dir
    `$ mkdir project`
    `$ cd project`
- create and activate virtualenv
    `$ python3 -m venv .venv`
    `$ . .venv/bin/activate`
- clone repository from [here](git@github.com:andreea0008/cc_server_side_python.git)
    `git clone git@github.com:andreea0008/cc_server_side_python.git`
- install the requirements
    `$ cd guide`
    `$ pip install -r requirements.txt`
- add settings_local.py file in  project/guide/guide/ with next local database settings. For example:
    ```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'guide_db',
            'USER': 'guide_db',
            'PASSWORD': 'some_pass',
            'HOST': 'localhost',
            'PORT': '',
        }
    }
    ENV_LABEL = 'local'
    ```
- make migrations
    `$ ./manage.py migrate`
- run server
    `$ ./manage.py runserver` (will be run on [localhost:8000](localhost:8000))


### Project file structure
- guide
