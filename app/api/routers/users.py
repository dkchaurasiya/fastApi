from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ... import schemas
from ..deps import get_user_service
import logging
import traceback

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=schemas.UserOut)
def create_user(user_in: schemas.UserCreate, user_service=Depends(get_user_service)):
    existing = user_service.get_by_email(user_in.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    try:
        return user_service.create(user_in)
    except Exception as e:
        logging.exception("Error creating user: %s", e)
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/", response_model=List[schemas.UserOut])
def list_users(skip: int = 0, limit: int = 100, user_service=Depends(get_user_service)):
    return user_service.list(skip, limit)


@router.get("/{user_id}", response_model=schemas.UserOut)
def get_user(user_id: int, user_service=Depends(get_user_service)):
    user = user_service.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
