from typing import List, Optional

from sqlalchemy.orm import Session

from fastapi.encoders import jsonable_encoder
from model.crud.base import CRUDBase
from model.models.model import Model
from model.schemas.model import Model as ModelSchema


class CRUDModel(CRUDBase[Model, ModelSchema]):
    """ Модель для CRUD операций по модели"""

    def save(self, db: Session, obj_in: ModelSchema) -> Model:
        """ Сохраняем модель в БД """
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        return self.create(db=db, obj_in=db_obj)


model = CRUDModel(Model)
