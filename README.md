# TeamGreenTea

a functional todoList application

#### Features
- In built authentication (logging in / signing up)
- In built Django Administration dashboard
- Simple todo list with logging for all CRUD Methods


##### How to start:
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
OR
```
docker-compose up
```

##### Migrations have an issue?
Try clearing the existing sqlite file (don't push please) and or read the above to reset all migration files
https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html
