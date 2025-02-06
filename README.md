# Q-CMS

The project is to create a Client Management Software, for a real estate agent. He wanna manage a database of clients, and a database of properties.

The software need to match the clients with the properties that could be corresponding to their requests. 

Here is a bunch of functionalities that it would need to have :

- [ ] Properties Management
  - [ ] Add, modify, delete a property (address, price, description, photos, etc.)
  - [ ] Categorize the property (apartment, house, land, etc.)
  - [ ] Search and filter the goods (by price, location etc)
- [ ] Client Management
  - [ ] Add customers (name, surname, birthday, email, phone, preferences)
  - [ ] Track interactions with each customer
- [ ] Calendar

## Disclaimer

I am a beginner in dev, and this is my first time creating an application. 

Also, I am french, so I am sorry if the english isn't perfect in here, plus my project might contain french words in it (even if I am trying to do everything in english !)

Any advice is welcome ! :)

## Tech Stack

- Backend :
  - Django Python
- Database :
  - MariaDB
- Frontend : 
  - HTML

## Requirements 

### VENV

This project is using Python, when you import it to your machine, you'll need to create your own venv : 

```shell
# cd to the folder that contain the project
python -m venv venv
```

Activate it :

```shell
# On Windows 
venv\Scripts\activate

# On linux / MacOS
source venv/bin/activate
```

And install the requirements for this project :

```shell
pip install -r requirements.txt
```

### Database

I am using a MariaDB database that runs on localhost. 

Create a new database on your MariaDB instance :

```
CREATE DATABASE qcms ;
```

### .env

Your .env needs to include 

```
DB_NAME= 'qcms' # database name 
DB_USER= # database user 
DB_PASSWORD= # database password
DB_HOST= # database host
DB_PORT= # database port
SECRET_KEY= # your django secret key
```

### Admin Access

Run the following command to create your superuser and be able to access the admin console :

```shell
python manage.py createsuperuser
```

## Running the app

To run the project, run this command :

```shell
# cd to the folder that contain the project
python manage.py runserver
```

And go to your navigator on the URL : http://127.0.0.1:8000/

Admin Console URL : http://127.0.0.1:8000/admin/ 

