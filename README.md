Peytalane
=========

Configure API
-------------

To be connected with API (Arel and Lpmng-core and Stripe), you have to edit 3 files:
 * config/keyArel.json
 * config/keyCore.json
 * config/keyStripe.json

Launch with Docker
-----------------

```
	docker-compose up
```



Use virtualenv (without docker)
--------------
```
    $ python3 -m venv env
    $ source env/bin/activate
```


Installation (without docker)
------------

```
    $ pip install -r requirements.txt
```

```
    $ python manage.py makemigrations peytalaneApp
```

```
    $ python manage.py migrate peytalaneApp
```

if you want to edit stylesheet:

```
    $ sudo npm install -g bower
```

```
    $ bower install
```

```
    $ sudo npm install -g sass
```



Create admin account
--------------------

```
    $ python manage.py createsuperuser --username <user_in_the_core>
```
Then type the password of this user.

Launch server (without docker)
-------------

```batch
    $ python manage.py runserver
```

Compile sass
------------
```
    $ sass scss/main.scss peytalaneApp/static/peytalaneApp/style.min.css --style compressed
```

TODO for the lan
----------------
* add session in the core
* Add a button to export food reservation into a clean csv file ~ok

TODO
----
* Add a page with the summary of all user's transactions
* Add some screenshots in the readme ;)
* Update the style to be reponsive

IDEAS
-----
* choose payment online or payment on-site ? 

