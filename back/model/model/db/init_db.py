from sqlalchemy.orm import Session

from .db import base  # noqa: F401

# make sure all SQL Alchemy models are imported (app_1.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # todo: add init db features
    pass
