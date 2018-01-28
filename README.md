Peytalane
=========

Installation
------------

```powershell
    $ pip install -r requirements.txt
```

```bash
    $ python manage.py makemigrations peytalaneApp
```

```sh
    $ python manage.py migrate peytalaneApp
```

if you want to edit stylesheet:

```zsh
    $ bower install
```

```csh
    $ gem install sass
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
* Display real foods which is order on resume section : info is store in `have_foods` var in `peytalaneApp/function/decorator.py`
* Do and /or verify all callback in `peytalaneApp/function/transaction.py`
* In each callback, store a summary of the transaction to the bdd, there is a model `payment`
* Do front-page for payment
* Do payment request to lydia api on /api/request/do
* When payment is valid:    
    - Transform request.sessions["transactions"] array to array of transactions object
    - For all transaction do transaction.payment
