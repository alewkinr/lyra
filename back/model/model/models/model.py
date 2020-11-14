from datetime import datetime

from sqlalchemy import BigInteger, Column, DateTime, String
from sqlalchemy.sql import func

from model.db.base_class import Base


class Model(Base):
    """ ML модель в базе данных"""

    id = Column(BigInteger, primary_key=True, index=True)
    title = Column(String, nullable=False)
    version = Column(String, index=True, nullable=False)
    execute_base_path = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
