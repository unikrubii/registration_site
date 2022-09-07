# The "Website"
A "website" (kind of). includes registration, login, and editing user's personal data with Django and Django-Ninja


## Getting started

1. Clone this repo.

2. Your Environment.
- Download Postgresql https://www.postgresql.org/download/ and install
- If you don't want to install Postgresql in your computer, use `Dev Container` in vscode
- Install pipenv `pip install pipenv`
- Run `pipenv install` or `pipenv sync`

3. Create .env file in root of this project.

.env file 
```
PG_DBNAME=database_name
PG_USER=database_user
PG_PASSWORD=database_password
PG_HOST=localhost (mostly)
PG_PORT=5432 (postgres default port)
```

4. Run `pipenv run python manage.py runserver` in your terminal

5. Click url on your terminal or type localhost:8000 in your browser

# Api services
<img width="1167" alt="image" src="https://user-images.githubusercontent.com/83582645/187141880-e3f87d38-cc1e-4c30-9419-24caa9093b11.png">
