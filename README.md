# 🛒 Cart Shop

A robust, full-stack e-commerce web application built to deliver a seamless online shopping experience. This project demonstrates end-to-end web development capabilities, featuring secure user authentication, dynamic product cataloging, and streamlined order management.

---

## 🏗️ Architecture (MVT Pattern)

Cart Shopee is built on Django's **Model-View-Template (MVT)** architecture, ensuring a clean separation of concerns between data, user interface, and application logic.

*   **Client (Frontend):** Users interact with the application through the browser using responsive HTML, CSS, and JavaScript interfaces.
*   **URLs & Views (The Controller):** Django intercepts the HTTP requests, routes them to the appropriate View, and processes the business logic (e.g., adding to cart, processing an order).
*   **Models (Data Layer):** The View interacts with Django's ORM to securely query and update the SQLite database (managing Products, CartItems, Orders, and Reviews).
*   **Templates (Presentation Layer):** The View passes the retrieved data to the Django Templates, which render the final dynamic HTML pages sent back to the user.

---

## 🚀 Features

*   **User Authentication & Authorization:** Secure login and registration workflows for customers.
*   **Dynamic Product Catalog:** Categorized product listings leveraging `Category` and `Product` models for scalable inventory management.
*   **Shopping Cart System:** Interactive cart functionality (`CartItem` model) allowing users to seamlessly add, review, and manage items before purchase.
*   **Order Processing & Tracking:** Comprehensive checkout system (`Order` model) with order status updates and history tracking.
*   **Customer Feedback:** Integrated product review (`Review` model) functionality to drive user engagement.
*   **Responsive Frontend:** Custom-styled interfaces using HTML, CSS (including specialized stylesheets like `home.css` and `about.css`), and JavaScript for an optimal user experience across devices.

---

## 💻 Tech Stack

*   **Backend:** Python, Django
*   **Frontend:** HTML5, CSS3, JavaScript
*   **Database:** SQLite3
*   **Architecture:** MVT (Model-View-Template)

---

## 🛠️ Installation & Local Setup

Follow these steps to run the project locally for development and testing.

### Prerequisites
*   Python 3.x installed on your machine.
*   Git installed.

### Steps

1. **Clone the repository**
   ```bash
   git clone [https://github.com/AlinAlexMyladoor/Cart_shop.git](https://github.com/AlinAlexMyladoor/Cart_shop.git)
   cd Cart_shop/myproject
