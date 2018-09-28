Peytalane
=========

Use virtualenv
--------------
```
    $ python3 -m venv env
    $ source env/bin/activate
```


Installation
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

to be connected with API (Arel and lpmng-core), you have to create two files:
 * peytalaneApp/keyArel.json
 * peytalaneApp/keyCore.json

```json
    {
        "key":"thekey",
        "app":"appName"
    }
```  
<span style="color:red"> **Peytalane is dependant of lpmng-core** </span>

you can edit lpmng-core url in ``` peytalaneApp/functions/core.py ```

Launch server
-------------

```batch
    $ python manage.py runserver
```

Compile sass
------------
```
    $ sass scss/main.scss peytalaneApp/static/peytalaneApp/style.min.css --style compressed
```

TODO
----
* Display real foods and tournament amready order on resume section (check the decorator)
* Do front-page for payment, do payment request to lydia api , clean transactions list
* Update front for tournament reservation
* Find a solution if a user had already reserved a tournament and want to change / (same for food ?)
* Do verification on post request for food reservation
* Add delete button on the aside with transactions list
* Create an admin page with the summary of all reservations
* Add some screenshots in the readme ;)