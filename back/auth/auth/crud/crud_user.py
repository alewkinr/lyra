from typing import Optional

from sqlalchemy.orm import Session

from auth.crud.base import CRUDBase
from auth.models.user import User
from auth.schemas.user import UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    """ Модель для CRUD операций по юзеру"""

    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        """Получаем пользователя по email"""
        return db.query(User).filter(User.email == email).first()

    def is_active(self, user: User) -> bool:
        """ Проверяем, что юзер активен """
        return user.is_active

    def is_superuser(self, user: User) -> bool:
        """ Проверяем, что юзер — admin"""
        return user.is_superuser


user = CRUDUser(User)
