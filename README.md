# Django Market Application

This Django project is a simple market application for managing products, categories, user accounts, and orders.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
      git clone https://github.com/yourusername/django-market-app.git
   
      cd django-market-app

Create a virtual environment and install dependencies:

    python -m venv venv
    
    source venv/bin/activate  
    
    On Windows, use 'venv\Scripts\activate'
    
    pip install -r requirements.txt

Apply database migrations:

    python manage.py migrate
    
Create a superuser account:

    python manage.py createsuperuser

Start the development server:

    python manage.py runserver


Access the application at http://localhost:8000/

## API Endpoints

### Home

Endpoint: /

Description: Renders the home page of the market application.

Method: GET

### Collections

Endpoint: /collections/

Description: Displays a list of available product categories.

Method: GET

### Collection View

Endpoint: /collections/<str:slug>/

Description: Displays products within a specific category.

Method: GET

### Product View

Endpoint: /collections/<str:cate_slug>/<str:prod_slug>/

Description: Displays detailed information about a product.

Method: GET

### User Registration

Endpoint: /register/

Description: Allows users to register for an account.

Method: POST

### User Login

Endpoint: /login/

Description: Allows users to log in to their accounts.

Method: POST

### User Logout

Endpoint: /logout/

Description: Allows users to log out from their accounts.

Method: GET

### Add to Cart

Endpoint: /add-to-cart

Description: Adds a product to the user's shopping cart.

Method: POST

### View Cart

Endpoint: /cart

Description: Displays the user's shopping cart.

Method: GET

### Update Cart

Endpoint: /update-cart

Description: Updates the quantities of products in the shopping cart.

Method: POST

### Delete Cart Item

Endpoint: /delete-cart-item

Description: Removes a product from the shopping cart.

Method: POST

### Wishlist

Endpoint: /wishlist

Description: Displays the user's wishlist.

Method: GET

### Add to Wishlist

Endpoint: /add-to-wishlist

Description: Adds a product to the user's wishlist.

Method: POST

### Delete Wishlist Item

Endpoint: /delete-wishlist-item

Description: Removes a product from the user's wishlist.

Method: POST

### Checkout

Endpoint: /checkout

Description: Displays the checkout page for placing orders.

Method: GET

### Place Order

Endpoint: /place-order

Description: Places an order for the products in the shopping cart.

Method: POST

### My Orders

Endpoint: /my-orders

Description: Displays a list of the user's orders.

Method: GET

### View Order

Endpoint: /view-order/<str:t_no>

Description: Displays detailed information about a specific order.

Method: GET

