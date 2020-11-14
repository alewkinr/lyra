# Import all the models, so that Base has them before being
# imported by Alembic
from model.db.base_class import Base  # noqa
from model.models.model import Model  # noqa
