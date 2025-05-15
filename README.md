# Gas Service Request – Django Project

This is a Django-based web application for managing gas service requests. It includes user authentication, service request management, and an admin panel for handling user accounts and service entries.

## 🚀 Features

- User registration and login
- Superuser/admin panel
- Request gas service functionality
- Django ORM with SQLite by default
- Clean code structure

## 🛠 Tech Stack

- **Backend**: Django 5.2.1 (Python)
- **Database**: SQLite (default)
- **Frontend**: Django templates (HTML/CSS)

## 📦 Installation

Follow the steps below to set up the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/yashpatel000007/gas-service-request-django.git
cd gas-service-request-django
```
### 2. Create and Activate Virtual Environment
On Windows (PowerShell):
```bash
python -m venv env
.\env\Scripts\Activate.ps1
```
On macOS/Linux:
```bash
python3 -m venv env
source env/bin/activate
```
### 3. Install Dependencies
```bash
pip install django
```
### 4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 5. Create Superuser
```bash
python manage.py createsuperuser
```
Follow the prompts to enter username, email, and password.

### 6. Run the Server
```bash
python manage.py runserver
```
# User Login Page
```bash
http://127.0.0.1:8000/accounts/login/
```
# Admin Login Page
```bash
http://127.0.0.1:8000/admin/login/
```

