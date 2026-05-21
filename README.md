# Django Todo API

A backend-only Todo API built with Django REST Framework and JWT Authentication.

## Features

- User registration
- JWT login
- CRUD tasks
- User can only manage their own tasks
- Admin/staff can view all tasks
- Filter tasks by completed, priority, due_date
- Search tasks by title
- Task summary API
- Mark task as completed API

## Tech Stack

- Python
- Django
- Django REST Framework
- Simple JWT
- SQLite
- Postman for API testing

## Installation

```bash
git clone <your-repo-url>
cd django_todo_api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

-----------------------------------------

API Endpoints

Auth:
POST /api/register/
POST /api/token/
POST /api/token/refresh/

Tasks:
GET    /api/tasks/
POST   /api/tasks/
GET    /api/tasks/{id}/
PATCH  /api/tasks/{id}/
DELETE /api/tasks/{id}/

Filters:
GET /api/tasks/?completed=true
GET /api/tasks/?priority=high
GET /api/tasks/?due_date=2026-05-25
GET /api/tasks/?search=django

Summary:
GET /api/tasks/summary/

Mark completed:
PATCH /api/tasks/{id}/mark-completed/

Example Create Task:
    {
    "title": "Learn Django REST Framework",
    "description": "Build a Todo API",
    "completed": false,
    "priority": "high",
    "due_date": "2026-05-25"
    }

