
# FastAPI CRUD with PostgreSQL

This project is a minimal FastAPI application demonstrating complete CRUD operations against a PostgreSQL database using SQLAlchemy.

Setup

1. Create a PostgreSQL database and user.
2. Set the `DATABASE_URL` environment variable. Example:

```
export DATABASE_URL="postgresql+psycopg://username:password@localhost:5432/dbname"
```

On Windows (PowerShell):

```
$env:DATABASE_URL = "postgresql+psycopg://username:password@localhost:5432/dbname"
```

Run the app

```
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API Endpoints

- `POST /items/` - create item
- `GET /items/` - list items
- `GET /items/{id}` - get item
- `PUT /items/{id}` - update item
- `DELETE /items/{id}` - delete item
