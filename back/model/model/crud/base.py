from typing import Any, Generic, List, Optional, Type, TypeVar

from sqlalchemy.orm import Session

from model.db.base_class import Base
from pydantic import BaseModel

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class
        """
        self.model = model

    def get(self, db: Session, _id: Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == _id).first()

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, *, obj_in: ModelType) -> ModelType:
        db.add(obj_in)
        db.commit()
        db.refresh(obj_in)
        return obj_in

    def remove(self, db: Session, *, _id: int) -> ModelType:
        obj = db.query(self.model).get(_id)
        db.delete(obj)
        db.commit()
        return obj
