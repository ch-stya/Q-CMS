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

Also, I am french, so I am sorry if the english isn't perfect in here, plus my project might contain french words in it.

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
# cd to the folder that contain the project (Q-CMS)
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

```sql
CREATE DATABASE qcms ;
```

### .env

Your .env needs to include 

```sql
DB_NAME= 'qcms' # database name 
DB_USER= # database user 
DB_PASSWORD= # database password
DB_HOST= # database host
DB_PORT= # database port
SECRET_KEY="" # your django secret key
```

### Django Key

To generate you own Django secret key, run the following command (inside the venv) :

```shell
# Windows 
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Linux
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

```

Copy and paste it in the .env file.

### Database update

To create the tables in the database, run the following command :

```shell
# cd to the folder that contain the project (Q-CMS/q_cms)
python manage.py migrate
```

### Admin Access

Run the following command to create your superuser and be able to access the admin console :

```shell
# cd to the folder that contain the project (Q-CMS/q_cms)
python manage.py createsuperuser
```

## Running the app

To run the project, run this command :

```shell
# cd to the folder that contain the project (Q-CMS/q_cms)
python manage.py runserver
```

And go to your navigator on the URL : http://127.0.0.1:8000/

Admin Console URL : http://127.0.0.1:8000/admin/ 

