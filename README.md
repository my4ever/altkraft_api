# altkraft_api
This is a task project for altkraft 

#### Install dependencies run:
     pip install -m requirements.txt

#### If you need more than 10 codes being stored in case of a flow of requests
    On line 128 in altkraft_api.altkraft_api.setting.py 
    set NUMBER_OF_VALID_CODE parameter

#### Make migrations run:
    python3 manage.py makemigrations

#### Apply migrations run:
    python3 manage.py migrate

#### If you need access into admin page run:
     python3 manage.py createsuperuser
and continue after filling all the required fields.
Address of the admin page by default is `127.0.0.1:8080/admin/`
    
#### In order to make project work:
     python3 manage.py runserver 8080

#### Now you can add urls into Database:
    127.0.0.1:8080/a/?url=PLASE-YOUR-URL-HERE

#### Go to url:
    127.0.0.1:8080/s/PLASE-YOUR-CODE-HERE
