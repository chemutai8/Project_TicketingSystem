# Django Ticketing System

A comprehensive ticketing system built with Django that allows users to browse events, purchase tickets, and manage their bookings.

## Features

- User Authentication (Register, Login, Logout)
- Event Management (Create, View, List)
- Ticket Management (Purchase, View, Cancel)
- Staff-only event creation
- Responsive Bootstrap UI
- Form validation and feedback
- Pagination for event listings

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd ticketing_system
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Apply database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Usage

1. Access the admin interface at `http://127.0.0.1:8000/admin/` to manage events and users
2. Register a new user account
3. Browse available events
4. Purchase tickets for events
5. View and manage your tickets

## Project Structure

```
ticketing_system/
├── events/                 # Events app
│   ├── models.py          # Event and Ticket models
│   ├── views.py           # View logic
│   ├── forms.py           # Forms for events and tickets
│   └── urls.py            # URL routing
├── users/                 # Users app
│   ├── views.py          # User-related views
│   ├── forms.py          # User registration forms
│   └── urls.py           # User URL routing
├── templates/            # HTML templates
│   ├── base.html        # Base template
│   ├── events/          # Event templates
│   └── users/           # User templates
└── manage.py            # Django management script
```

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.