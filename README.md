# FeedBook Demo API

A backend REST API built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL (Supabase)** to learn modern backend development practices. This project serves as a hands-on sandbox for implementing real-world backend concepts such as layered architecture, database relationships, migrations, authentication, and API design.

---

# 🚀 Tech Stack

## Backend

- Python
- FastAPI

## Database

- PostgreSQL (Supabase)

## ORM

- SQLAlchemy

## Database Migrations

- Alembic

## Validation

- Pydantic

## Configuration

- Pydantic Settings
- python-dotenv

## Database Driver

- psycopg2

## Backend-as-a-Service

- Supabase

---

# 📦 Features

## CRUD Operations

### Person

- ✅ Create
- ✅ Read
- ✅ Read by ID
- ✅ Update
- ✅ Delete
- ✅ Pagination

### Dog

- ✅ Create
- ✅ Read
- ✅ Read by ID
- ✅ Delete
- ✅ Pagination

---

# 🗄️ Database Features

- ✅ SQLAlchemy ORM
- ✅ One-to-Many Relationships (Person → Dogs)
- ✅ Foreign Keys
- ✅ Alembic Database Migrations
- ✅ PostgreSQL (Supabase)

---

# 📅 Development Log

## 06/24/26

- Added Dog model
- Added search by ID for Person and Dog

## 06/25/26

- Added delete endpoints
- Added update endpoint for Person

## 06/26/26

- Added pagination for Person and Dog

## 06/27/26

- Integrated Alembic
- Implemented one-to-many relationships using SQLAlchemy
- Connected Person and Dog models with Foreign Keys and `relationship()`

---

# 🧠 Learning Roadmap

## 🔐 Authentication

- Password hashing (bcrypt / passlib)
- User registration
- User login
- JWT Authentication
- Protected routes

## 👤 Authorization

- Role-based authorization
- Ownership-based authorization

## 🗄️ Database

- Cascade delete/update
- Advanced SQLAlchemy relationships
- Better schema design
- Database indexing

## ⚙️ Backend Architecture

- Repository Pattern
- Service Layer
- Centralized exception handling
- Standardized API responses

## 🧪 Testing

- Pytest
- CRUD unit tests
- Test database configuration

## 📈 DevOps

- Docker
- Environment separation
- CI/CD basics
- Deployment (Render / Railway / AWS)

---

# 📌 Project Philosophy

This repository is a learning-focused backend project that evolves over time. Instead of building multiple disconnected demos, new backend concepts are continuously integrated into a single codebase to simulate the growth of a real production application.

---

# 📝 Notes

- Uses Alembic for schema versioning and migrations.
- Uses PostgreSQL hosted on Supabase.
- Follows a layered architecture (API → Service → Repository).
- Built primarily for learning backend engineering best practices.

---

# 🔮 Next Milestone

Implement a complete authentication system featuring:

- Password hashing
- User registration
- User login
- JWT access tokens
- Protected API endpoints
- User model integration with existing relationships
