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
* Do front-page for payment, do payment request to lydia api , clean transactions list
* Find a solution if a user had already reserved a tournament and want to change / (same for food ?)
* Create an admin page with the summary of all reservations ~done
* Update the style to be reponsive
* Do the search for foods
* Add a page with the summary of all user's transactions
* Add some screenshots in the readme ;)

IDEAS
-----
* choose payment online or payment on-site ? 
