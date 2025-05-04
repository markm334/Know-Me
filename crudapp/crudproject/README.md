# CRUD Project for Farmers

This project is a Django application designed to manage a platform for farmers. It includes features for user registration, product management, and a wishlist system.

## Project Structure

```
crudproject
├── crudproject
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── crudapp
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd crudproject
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install django
   ```

4. **Run migrations:**
   ```
   python manage.py migrate
   ```

5. **Create a superuser:**
   ```
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```
   python manage.py runserver
   ```

## Usage

- Access the application at `http://127.0.0.1:8000/`.
- Admin panel can be accessed at `http://127.0.0.1:8000/admin/`.

## Features

- Custom user model for farmers.
- Product management.
- Wishlist functionality.
- User registration and authentication.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.