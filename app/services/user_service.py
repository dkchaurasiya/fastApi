from passlib.context import CryptContext
from sqlalchemy.orm import Session
from .. import schemas
from ..crud import users as crud_users


pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")


class UserService:
    def __init__(self, db: Session):
        self.db = db

    def get(self, user_id: int):
        return crud_users.get_user(self.db, user_id)

    def get_by_email(self, email: str):
        return crud_users.get_user_by_email(self.db, email)

    def create(self, user_in: schemas.UserCreate):
        hashed = pwd_context.hash(user_in.password)
        return crud_users.create_user(self.db, email=user_in.email, hashed_password=hashed, full_name=user_in.full_name)

    def authenticate(self, email: str, password: str):
        user = self.get_by_email(email)
        if not user:
            return None
        if not pwd_context.verify(password, user.hashed_password):
            return None
        return user

    def list(self, skip: int = 0, limit: int = 100):
        return crud_users.get_users(self.db, skip, limit)
