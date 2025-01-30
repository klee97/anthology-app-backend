#  Backend server with Django + Postgres

This is a Django project with a Postgres DB.


## Getting Started

### 1. Set up a virtual environment
```
# On macOS/Linux:
python3 -m venv venv

# On Windows:
python -m venv venv
```

### 2. Activate the virtual environment
```
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

You should now see (venv) at the beginning of your terminal prompt, indicating that the virtual environment is active.

### 3. Install the requirements
```
pip install -r requirements.txt
```

### 4. Set up local database
Start Postgres
```
brew services start postgresql

```

Run the migrations based on your Django models to create the database tables:
```
python manage.py migrate
```

Seed the story data
```
python manage.py import_stories tmp/lightspeed_stories.csv 
```

Optional: Test your import
```
python manage.py shell
>>> from stories.models import Story

# Find all Stories
>>> Story.objects.all()
<QuerySet [...]>
```

### 5. Run the server
```
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) with your browser to see the [admin site](https://docs.djangoproject.com/en/5.1/ref/contrib/admin/).

### 6. Log in to the admin site

On the admin site, log in with your credentials. If you don't have credentials, you can create a superuser by running

```
python manage.py createsuperuser
```

## To do

- [x] Add Postgres db and a stories table
- [x] Import scraped story metadata in Postgres (Lightspeed only for now)
- [x] Create a Story model, run migration, and register Story with admin
- [] Add API endpoints to the Story model for Next.js integration (using Django REST Framework?)
- [] Standardize the publishing date for story metadata