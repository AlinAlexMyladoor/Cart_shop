# 🛒 Cart Shop

> A full-stack e-commerce web application built with **Python and Django**, providing product discovery, category-based filtering, session-based shopping cart management, checkout, order tracking, and customer feedback.

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2-green?logo=django)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-blue?logo=sqlite)](https://www.sqlite.org/)
[![GitHub](https://img.shields.io/badge/Source-GitHub-black?logo=github)](https://github.com/AlinAlexMyladoor/Cart_shop)

---

## 📌 Overview

**Cart Shop** is a Django-based e-commerce platform that implements the core workflow of an online shopping system.

Customers can register, authenticate, browse and filter products, manage their shopping cart, place individual or multiple-product orders, track order status, cancel orders, and submit ratings and feedback.

The application also provides administrative functionality for managing **users, products, categories, and orders**.

---

## ✨ Features

### 👤 Customer

* User registration and login
* Custom Django user model
* Product browsing
* Category-based product filtering
* Price-based filtering
* Product image display
* Session-based shopping cart
* Add, remove, and update cart quantities
* Individual product checkout
* Cart-wide checkout
* Delivery address management
* Order history
* Order status tracking
* Order cancellation
* Product ratings and feedback

### 🔐 Administration

* User management
* Product CRUD operations
* Product image uploads
* Category management
* View customer orders
* Update order status
* Monitor pending and cancelled orders

---

## 🏗️ Architecture

The application follows Django's **MVT (Model–View–Template)** architecture.

```text
                         ┌─────────────────┐
                         │      User       │
                         │   Web Browser   │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │   URL Routing   │
                         │  Django URLs    │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │      Views      │
                         │ Business Logic  │
                         └───────┬───┬─────┘
                                 │   │
                    ┌────────────┘   └────────────┐
                    ▼                             ▼
             ┌──────────────┐             ┌──────────────┐
             │    Models    │             │   Templates  │
             │  Django ORM  │             │   HTML/CSS   │
             └──────┬───────┘             └──────┬───────┘
                    │                            │
                    ▼                            │
             ┌──────────────┐                    │
             │    SQLite    │                    │
             │   Database   │                    │
             └──────────────┘                    │
                                                 ▼
                                          ┌──────────────┐
                                          │ HTTP Response│
                                          └──────────────┘
```

### Application Flow

```text
Register / Login
       ↓
Browse Products
       ↓
Filter by Category / Price
       ↓
Add to Cart
       ↓
Update Quantity
       ↓
Checkout
       ↓
Create Order
       ↓
Track Order
       ↓
Rating & Feedback
```

---

## 🛠️ Tech Stack

| Layer               | Technologies                              |
| ------------------- | ----------------------------------------- |
| **Backend**         | Python, Django 5.2                        |
| **Frontend**        | HTML5, CSS3, JavaScript, Django Templates |
| **Database**        | SQLite                                    |
| **ORM**             | Django ORM                                |
| **Authentication**  | Django Authentication & Sessions          |
| **Forms**           | Django Forms                              |
| **Media**           | Django ImageField / Media Storage         |
| **Version Control** | Git, GitHub                               |

---

## 📁 Project Structure

```text
Cart_shop/
│
├── myproject/
│   ├── manage.py
│   │
│   ├── myproject/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   ├── myapp/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── forms.py
│   │   ├── urls.py
│   │   ├── admin.py
│   │   ├── migrations/
│   │   ├── templates/
│   │   └── static/
│   │
│   ├── media/
│   │   └── product_images/
│   │
│   └── db.sqlite3
│
└── README.md
```

---

## 🗄️ Data Model

The core entities are designed around users, products, categories, cart items, and orders.

```text
┌──────────────┐
│    User      │
└──────┬───────┘
       │
       ├─────────────────┐
       ▼                 ▼
┌──────────────┐   ┌──────────────┐
│  Cart Item   │   │    Order     │
└──────┬───────┘   └──────┬───────┘
       │                  │
       └─────────┬────────┘
                 ▼
          ┌──────────────┐
          │   Product    │
          └──────┬───────┘
                 │
                 ▼
          ┌──────────────┐
          │   Category   │
          └──────────────┘
```

### Core Models

* **Register** — Custom user model based on Django `AbstractUser`
* **Product** — Product name, category, price, and image
* **Category** — Product categorization
* **CartItem** — Product quantity associated with a user
* **Order** — Product, quantity, address, status, rating, and feedback

---

## 🛒 Shopping Cart

The cart is implemented using Django's **session framework**, allowing users to maintain their cart without requiring a separate persistent cart record for every session.

```text
Add Product
     ↓
Session Cart
     ↓
Update Quantity
     ↓
Calculate Subtotal
     ↓
Calculate Total
     ↓
Checkout
     ↓
Create Order
     ↓
Clear Cart
```

---

## 📦 Order Management

Orders follow a simple lifecycle:

```text
┌──────────┐
│  Placed  │
└────┬─────┘
     │
     ▼
┌──────────┐
│ Shipped  │
└────┬─────┘
     │
     ▼
┌──────────┐
│Delivered │
└──────────┘

     OR

┌──────────┐
│Cancelled │
└──────────┘
```

Each order stores:

* Customer
* Product
* Quantity
* Delivery address
* Order timestamp
* Order status
* Customer rating
* Customer feedback

---

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/AlinAlexMyladoor/Cart_shop.git
cd Cart_shop
```

### 2. Create a virtual environment

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install django pillow
```

### 4. Navigate to the Django project

```bash
cd myproject
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Create an administrator account

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open the application at:

```text
http://127.0.0.1:8000/
```

Admin panel:

```text
http://127.0.0.1:8000/admin/
```

---

## 💡 Engineering Concepts

This project demonstrates practical implementation of:

* Django MVT architecture
* Custom user models
* Django authentication
* Session-based state management
* Django ORM
* Relational database modeling
* CRUD operations
* Django Forms
* Form validation
* File and image uploads
* Product filtering
* Shopping cart business logic
* Checkout workflows
* Order lifecycle management
* Customer reviews and ratings
* Database migrations
* Server-side template rendering

---

## 🚀 Future Improvements

* Django REST Framework API
* PostgreSQL production database
* Redis caching
* Payment gateway integration
* Product search and pagination
* Wishlist functionality
* Inventory management
* Email notifications
* Automated testing
* Docker containerization
* CI/CD pipeline
* Cloud deployment

---

## 👨‍💻 Author

### Alin Alex

Computer Science & Engineering Student
Christ College of Engineering, Kerala

**GitHub:**
https://github.com/AlinAlexMyladoor

**Project Repository:**
https://github.com/AlinAlexMyladoor/Cart_shop

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐.
