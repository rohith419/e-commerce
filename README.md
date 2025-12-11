# E-Commerce Project (Django REST + Vue 3)

This repository is a **starter scaffold** for a full-stack e-commerce site:
- **Backend:** Django + Django REST Framework + Simple JWT
- **Frontend:** Vue 3 + Vite + Tailwind (minimal setup)

This scaffold includes:
- Product model, APIs (list, retrieve, create)
- Simple User registration/login via JWT
- Cart & Order basic models and endpoints (starter)
- Vue frontend with product listing, product details, cart, auth scaffolding

## How to run (Backend)

1. Create and activate a virtualenv:
```bash
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
```

2. Install backend requirements:
```bash
pip install -r backend/requirements.txt
```

3. Run migrations and start server:
```bash
cd backend
python manage.py migrate
python manage.py runserver
```
By default the API runs at http://127.0.0.1:8000/

## How to run (Frontend)

1. Install dependencies:
```bash
cd frontend
npm install
npm run dev
```
The dev server runs on http://localhost:5173/ by default.

## Notes
- This is a scaffold: extend models, validations, admin and frontend UI as needed.
- For auth we used djangorestframework-simplejwt — configure `ALLOWED_HOSTS`, static/media settings, and CORS for production.

Enjoy! 🚀
