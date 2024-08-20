from sqlalchemy import select

from database.session import Session
from models.user import User
from utils.base_model import AbstractBaseModel
from utils.generic_controller import GenericController
from utils.security import get_password_hash


class UserController(GenericController):
    def __init__(self) -> None:
        super().__init__(User)

    def get_user_by_username(self, db_session: Session, username: str) -> User:
        return db_session.scalar(select(User).where(User.username == username))

    def save(self, db_session: Session, obj: User) -> AbstractBaseModel:
        obj.password = get_password_hash(obj.password)
        return super().save(db_session, obj)

    def update(self, db_session: Session, obj: User) -> AbstractBaseModel:
        obj.password = get_password_hash(obj.password)
        return super().update(db_session, obj)
