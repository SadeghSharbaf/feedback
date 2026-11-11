# Feedback Platform

A Django application for collecting and browsing user reviews, viewing individual review details, marking a review as a session-based favorite, and creating simple user profiles with uploaded profile images.

## Features

- Submit a review with a user name, review text, and rating.
- Display a list of submitted reviews.
- View an individual review.
- Mark a review as a favorite using the visitor's session.
- Show a thank-you page after a successful submission.
- Create and list user profiles with uploaded images.
- Django admin integration.

## Technology

- Python
- Django (project settings generated with Django 5.1.1)
- SQLite for local development
- Django templates and media uploads
- Pillow is required for image-field support.

## Project structure

```text
feedback/
├── feedback/       # Django project settings and root URLs
├── reviews/        # Review model, forms, views, and URLs
├── profiles/       # User profile model, forms, views, and URLs
├── uploads/        # Local uploaded media (runtime data)
└── manage.py
```

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/SadeghSharbaf/feedback.git
cd feedback
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

The repository currently does not include a `requirements.txt` file. Install Django and Pillow:

```bash
python -m pip install "Django==5.1.1" Pillow
```

### 4. Create the database

```bash
python manage.py migrate
```

### 5. Create an administrator (optional)

```bash
python manage.py createsuperuser
```

### 6. Start the development server

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/.

## Main routes

| Route | Description |
| --- | --- |
| `/` | Review submission form |
| `/thank-you` | Submission confirmation |
| `/reviews` | Review list |
| `/reviews/<id>` | Individual review |
| `/reviews/favorite` | Session favorite action (POST) |
| `/profiles/` | Profile creation and listing routes are included under this prefix |
| `/admin/` | Django administration |

## Data models

- **Review** — user name, review text, and integer rating.
- **UserProfile** — uploaded profile image.

## Production checklist

The checked-in settings are development-oriented: they contain an in-source development secret key, set `DEBUG = True`, and leave `ALLOWED_HOSTS` empty. Before deployment:

- Move `SECRET_KEY` into environment configuration and replace it with a strong private value.
- Set `DEBUG = False` and configure allowed hosts.
- Add validation and sensible bounds for ratings and submitted text.
- Add authentication, authorization, and moderation controls if profiles or reviews should be restricted.
- Configure HTTPS, secure cookies, persistent media storage, and a production database.
- Keep uploaded media and private data out of version control.

## License

No license is currently specified in this repository.
