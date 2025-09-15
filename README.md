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

## 🛠 Tech Stack
- **Backend:** Django Rest Framework (DRF)
- **Database:** PostgreSQL
- **Auth:** JWT via djangorestframework-simplejwt
- **Docs:** drf-yasg (Swagger/OpenAPI)

---

## Project Structure
```bash
cms-api/
│── apps/
│   └── blog/        # Example CMS module
│── cms_api/         # Project settings
│── docs/            # ERDs, endpoint docs
│── requirements.txt # Dependencies
