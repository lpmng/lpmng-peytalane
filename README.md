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

to use stripe to pay you need a file keyStripe.json

```json
    {
        "private":"private_key",
        "public":"public_key"
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

