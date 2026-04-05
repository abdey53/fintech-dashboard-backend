# 💰 Finance Backend API

## 📌 Overview
This project is a backend system for managing financial records with **role-based access control**.

It is designed to simulate a real-world finance dashboard where different users (Admin, Analyst, Viewer) interact with financial data based on permissions.

---

## 🚀 Tech Stack
- Django
- Django REST Framework (DRF)
- SQLite
- JWT Authentication

---

## ✨ Features
- 👤 User Role Management (Admin, Analyst, Viewer)
- 🔐 Role-Based Access Control
- 💳 Financial Records CRUD (Create, Read, Update, Delete)
- 📊 Dashboard Analytics:
  - Total Income
  - Total Expense
  - Net Balance
  - Category-wise Summary
  - Monthly Trends
- 🔍 Filtering (type, category, date range)
- 📄 Pagination Support
- ⚠️ Input Validation & Error Handling

---

## 🔐 Authentication

This API uses **JWT (JSON Web Token)** authentication.


---

## 📡 API Endpoints

### 👥 Users (Admin Only)
- `GET /api/users/`
- `POST /api/users/`

---

### 💳 Financial Records
- `GET /api/records/`
- `POST /api/records/`
- `PUT /api/records/{id}/`
- `DELETE /api/records/{id}/`

#### 🔍 Filters:


---

### 📊 Dashboard APIs
- `GET /api/dashboard/summary/`
- `GET /api/dashboard/categories/`
- `GET /api/dashboard/trends/`
- `GET /api/dashboard/recent/`

---

## 📦 Sample Response

### Dashboard Summary
```json
{
  "total_income": 50000,
  "total_expense": 20000,
  "balance": 30000
}

---

### 📊 Dashboard APIs
- `GET /api/dashboard/summary/`
- `GET /api/dashboard/categories/`
- `GET /api/dashboard/trends/`
- `GET /api/dashboard/recent/`

---

## 📦 Sample Response

### Dashboard Summary
```json
{
  "total_income": 50000,
  "total_expense": 20000,
  "balance": 30000
}

⚙️ Setup Instructions
Clone the repository:
git clone https://github.com/your-username/fintech-dashboard-backend.git
cd fintech-dashboard-backend
Create virtual environment:
python -m venv venv
venv\Scripts\activate
Install dependencies:
pip install -r requirements.txt
Run migrations:
python manage.py migrate
Create superuser:
python manage.py createsuperuser
Run server:
python manage.py runserver

🧠 Assumptions
Roles are predefined (Admin, Analyst, Viewer)
Only Admin can modify users and financial records
Analysts can view records and analytics
Viewers can only view dashboard data
📁 Project Structure
finance-backend/
│── core/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── permissions.py
│   ├── urls.py
│── config/
│── manage.py

### للحصول على token:
