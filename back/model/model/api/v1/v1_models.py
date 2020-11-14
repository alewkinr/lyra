from typing import Any, Optional

from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException, Response, status
from model import crud, schemas
from model.api import deps
from model.core import errors, response

router = APIRouter()

# лимит на кол-во обхектов, получаемых из БД
DB_LIMIT = 500


@router.get("/", response_model=schemas.Model)
def find_models(model_id: Optional[int], db: Session = Depends(deps.get_db)) -> Any:
    # todo: разобраться с типом Optional[schemas.Model, List[schemas.Model]]
    """ Получаем описание ML-моделей по ID или списком """
    try:
        if not model_id:
            models = crud.model.get_multi(db=db, skip=0, limit=DB_LIMIT)
            if not models:
                return response.NoContentResponse()

            return models

        if model_id:
            model = crud.model.get(db=db, _id=model_id)
            if not model_id:
                return response.NoContentResponse()
            return model

    except Exception as err:
        raise errors.InternalServerErr(detail=err)


@router.post("/", response_model=schemas.Model)
def save_new_model(
    model: schemas.Model, db: Session = Depends(deps.get_db)
) -> schemas.Model:
    """ Создание новой ML-модели """
    try:
        model_in_db = crud.model.save(db, model)
        if not model_in_db:
            raise errors.InternalServerErr(detail="error to save model to db")
    except Exception as err:
        raise errors.InternalServerErr(detail=err)

    return model_in_db


@router.delete("/", response_model=schemas.Model)
def save_new_model(
    model_id: Optional[int], db: Session = Depends(deps.get_db)
) -> schemas.Model:
    """ Удаление существующей ML-модели """
    try:
        model = crud.model.get(db, _id=model_id)
        if not model:
            raise response.NoContentResponse()

        return crud.model.remove(db=db, _id=model_id)

    except Exception as err:
        raise errors.InternalServerErr(detail=err)
