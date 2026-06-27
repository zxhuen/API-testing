# FeedBook Demo API

A backend API built with FastAPI, SQLAlchemy, and PostgreSQL (Supabase), focused on learning backend development fundamentals such as CRUD, database migrations, and authentication.

---

## 🚀 Tech Stack

### Backend

- Python
- FastAPI

### Database

- PostgreSQL (Supabase)

### ORM

- SQLAlchemy

### Migrations

- Alembic

### Validation

- Pydantic

### Configuration

- Pydantic Settings
- dotenv

### Database Driver

- psycopg2

### Backend-as-a-Service

- Supabase

---

## 📦 Features Implemented

### (06/24/26)

- Added Dog model
- Added search by ID (Person & Dog)

### (06/25/26)

- Added delete (Dog & Person)
- Added update/edit (Person)

### (06/26/26)

- Added pagination (Dog & Person)

### (06/27/26)

- Integrated Alembic for database migrations

---

## 🧠 Learning Roadmap (In Progress)

### 🔐 Authentication & Security

- Password hashing (bcrypt / passlib)
- User registration & login system
- JWT authentication
- Protected routes (auth middleware / dependencies)

### 👤 Authorization

- Role-based access control (admin / user)
- Ownership-based permissions (user-specific data access)

### 🗄️ Database & ORM Improvements

- One-to-many relationships (e.g., User → Dogs)
- Foreign keys & cascading rules
- Improved schema design practices

### ⚙️ Backend Architecture

- Service layer separation
- Repository pattern (clean database access)
- Centralized error handling
- Consistent API response structure

### 🧪 Testing

- Pytest setup
- Unit tests for CRUD operations
- Test database configuration

### 📈 DevOps (Future)

- Docker containerization
- Environment-based configuration (dev/staging/prod)
- Deployment (Render / Railway / AWS basics)

---

## 🧪 Project Philosophy

This project is used as a **learning sandbox** to progressively build real-world backend engineering skills by evolving a single codebase over time.

---

## 📌 Notes

- Database schema is managed using Alembic migrations (no `create_all` in production flow)
- Supabase is used as hosted PostgreSQL
- Project will continuously evolve with new backend concepts

---

## 🔮 Next Step

Implement authentication system (JWT + password hashing)
