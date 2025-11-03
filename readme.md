Multi-Vendor Marketplace (Django + Stripe)

This is a simple multi-vendor marketplace built with Django. Vendors can list products, and users can purchase them through a Stripe Checkout flow. When a payment succeeds, the order is recorded and marked as paid. The purpose of the project is to learn backend development, database modeling, and how real payment systems work.

Features

Vendors can add and manage products.

Users can view product listings and make purchases.

Secure payment flow using Stripe Checkout.

Payment is verified using Stripe's Payment Intent.

Orders are stored and marked as paid only after Stripe confirms the payment.

Simple and clean Django backend structure.

Tech Stack

Backend: Python, Django
Database: SQLite (can be replaced with PostgreSQL)
Payment: Stripe Checkout + Payment Intent
Frontend: HTML, CSS, Bootstrap
Tools: Git, GitHub, VS Code

How the Payment Flow Works

The user selects a product and clicks "Buy".

A Stripe Checkout Session is created.

The user completes the payment on Stripe's page.

Stripe returns a session id.

The server checks the session and updates the order record.

The order is marked as paid only if Stripe confirms the payment was successful.

This makes sure there are no fake or incomplete order entries.

Project Structure
mysite/
 ├── mysite/        # Project settings
 ├── myapp/         # Main app (views, models, urls)
 ├── templates/     # HTML templates
 ├── uploads/       # Product images
 └── manage.py

Setup Instructions

Clone the repository:

git clone https://github.com/vidhi18-git/Marketplace-app.git
cd Marketplace-app/mysite


Create and activate a virtual environment:

python -m venv env
env\Scripts\activate  (Windows)


Install dependencies:

pip install -r requirements.txt


Create a .env file and add your Stripe test secret key:

STRIPE_SECRET_KEY=your_test_key_here


Apply migrations:

python manage.py migrate


Run the development server:

python manage.py runserver

What Can Be Improved Next

Add vendor dashboard to view sales.

Add cart and multiple product checkout.

Add Razorpay support for India.

Improve UI and product detail pages.

Add product categories and search.

Author

Vidhi Kashyap
Backend Development (Python + Django)
GitHub: https://github.com/vidhi18-git