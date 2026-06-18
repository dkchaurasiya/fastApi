from fastapi import FastAPI
from .database import engine, Base
from . import models
from .api.routers import items as items_router, users as users_router


app = FastAPI(title="FastAPI CRUD with PostgreSQL")


# Create database tables on startup (safe: won't run at import-time)
@app.on_event("startup")
def on_startup():
	try:
		Base.metadata.create_all(bind=engine)
	except Exception as e:
		import logging

		logging.warning("Could not create database tables on startup: %s", e)


# Include routers
app.include_router(items_router.router)
app.include_router(users_router.router)

