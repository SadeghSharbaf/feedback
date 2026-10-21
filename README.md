# Feedback Platform

A Django web application organized around feedback/reviews and user profiles.

## Tech Stack
- Python
- Django

## Getting Started
1. Create and activate a virtual environment.
2. Install dependencies from the project's dependency file, if present.
3. Configure local environment variables and database settings.
4. Initialize the database and run the application:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## Database
The local SQLite database is excluded from version control. Use migrations to create a fresh local database.

## Security
Do not commit credentials, secret keys, user records, or production data.
