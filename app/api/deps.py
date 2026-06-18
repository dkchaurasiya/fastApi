from typing import Generator
from fastapi import Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..services.user_service import UserService


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user_service(db: Session = Depends(get_db)) -> Generator:
    yield UserService(db)
