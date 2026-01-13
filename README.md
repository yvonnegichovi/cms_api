# CMS API (Django Rest Framework + PostgreSQL)

A **Content Management System (CMS) API** built with Django Rest Framework (DRF) and PostgreSQL.
This project demonstrates how to design and implement a scalable backend system with clean architecture, relational database modeling, JWT authentication, and automated API documentation.

---

## 🚀 Features

* **User Authentication** – JWT-powered auth using `djangorestframework-simplejwt`.
* **Blog Management** – CRUD endpoints for posts, categories, and tags.
* **Database Design** – Relational schema with UUID primary keys for scalability.
* **Timestamps** – `created_at` and `updated_at` columns for versioning and auditing.
* **Advanced Queries** – Pagination, filtering, and search.
* **API Documentation** – Interactive docs with Swagger (via `drf-yasg` or `drf-spectacular`).
* **Testing** – Unit tests for core endpoints to ensure reliability.

---

## 🛠️ Tech Stack

* **Backend:** Django Rest Framework (DRF)
* **Database:** PostgreSQL + PostGIS extension (for future geospatial queries)
* **Auth:** JWT via `djangorestframework-simplejwt`
* **Docs:** Swagger/OpenAPI (drf-spectacular / drf-yasg)

---

## ⚙️ Setup Instructions

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure PostgreSQL

Log into `psql` as a superuser and create the database + user:

```sql
CREATE DATABASE cms_db;
CREATE USER cms_user WITH PASSWORD 'cms_password';
ALTER ROLE cms_user SET client_encoding TO 'utf8';
ALTER ROLE cms_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE cms_user SET timezone TO 'UTC';
\c cms_db
CREATE EXTENSION postgis;
GRANT ALL PRIVILEGES ON DATABASE cms_db TO cms_user;
```

### 3. Update `settings.py`

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

### 4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the server

```bash
python manage.py runserver 8001
```

API docs will be available at:
👉 `http://127.0.0.1:8001/api/schema/swagger-ui/`

---

## 📌 Example Endpoints

* `POST /api/auth/login/` – Obtain JWT token.
* `GET /api/blog/posts/` – List all posts.
* `POST /api/blog/posts/` – Create a new post.
* `GET /api/blog/posts/{id}/` – Retrieve a post by UUID.

---

## 🎯 What This Project Demonstrates

* **Software Engineering Skills**: Database schema design, modular Django apps, separation of concerns.
* **API-first Development**: OpenAPI/Swagger integration for clear documentation.
* **Scalability Considerations**: UUIDs for distributed environments, PostGIS-ready database for geospatial queries.
* **Professional Practices**: Testing, version control, and environment-specific settings.

---

## 📷 Screenshots

*Add Swagger UI / API testing screenshots here for extra impact.*

---

## 📂 Repository

[GitHub Repo Link](#)

(Optional: Add a live demo link if deployed)
