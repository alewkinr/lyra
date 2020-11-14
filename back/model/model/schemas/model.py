from pydantic import BaseModel, Field


class Model(BaseModel):
    """ Схема ML-модели """

    id: int
    title: str
    execute_base_path: str
    version: str
