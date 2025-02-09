from sqlalchemy.ext.declarative import as_declarative, declared_attr
from db.base import Base

@as_declarative()
class Base:
    id: int
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
# Import all models here to ensure they are registered with SQLAlchemy
from db.models.user import User
from db.models.produce import Produce
from db.models.forum import ForumPost
from db.models.equipment import Equipment