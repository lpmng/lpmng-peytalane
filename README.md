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
