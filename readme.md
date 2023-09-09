API routes:
/api/menu
/api/booking

To make a GET request, the user must be authenticated
To make a POST request, the user must be a staff

To create a user and login:
1. Make a POST request to /auth/users with username and password as the body
2. Make a POST request to /auth/token/login

Alternatively, you can use `python manage.py createsuperuser` and do anything via the admin panal.

Please configure the MySQL database:
1. Create the database with the name mentioned in `settings.py` file
2. Change the password to match your database password
