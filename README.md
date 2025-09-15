# CMS API (Django Rest Framework + PostgreSQL)

A Content Management System (CMS) API built with **Django Rest Framework** and **PostgreSQL**.  
This project demonstrates **CRUD operations, authentication, relational database design, and API documentation**.

---

## Features
- User authentication (JWT)
- CRUD for posts, categories, and tags
- PostgreSQL relational schema
- Pagination, filtering, and search
- API documentation with DRF & Swagger
- Unit tests for core endpoints

---

## Tech Stack
- **Backend:** Django Rest Framework (DRF)
- **Database:** PostgreSQL
- **Auth:** JWT via djangorestframework-simplejwt
- **Docs:** drf-yasg (Swagger/OpenAPI)

---

## Database Setup
---

### 1️ Install PostgreSQL driver in your venv

```bash
pip install psycopg2-binary
```

Add it to your `requirements.txt`:

```txt
psycopg2-binary
```

---

### 2️ Create PostgreSQL database + user

From terminal:

```bash
psql -U postgres
```

Inside `psql`:

```sql
CREATE DATABASE cms_db;
CREATE USER cms_user WITH PASSWORD 'cms_password';
ALTER ROLE cms_user SET client_encoding TO 'utf8';
ALTER ROLE cms_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE cms_user SET timezone TO 'UTC';
\c suivi_db
CREATE EXTENSION postgis;
GRANT ALL PRIVILEGES ON DATABASE cms_db TO cms_user;
```

Exit with:

```
\q
```

---

### 3️ Update Django settings.py

Open `cms_api/settings.py` and replace the database config:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cms_db',
        'USER': 'cms_user',
        'PASSWORD': 'cms_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

### 4️ Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---
