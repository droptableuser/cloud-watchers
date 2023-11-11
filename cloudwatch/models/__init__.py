from ast import excepthandler
from multiprocessing.sharedctypes import Value
import uuid
from sqlalchemy_utils import UUIDType
from flask_sqlalchemy import SQLAlchemy
from cloudwatch.utils import db

def get_uuid(): 
    return str(uuid.uuid4())

def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
    except ValueError:
        return False
    return True

class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(
        UUIDType(binary=False), primary_key=True, nullable=False, default=get_uuid
    )
    created_at = db.Column(
        db.DateTime(timezone=True), default=db.func.now(), nullable=False, index=True
    )

    def to_dict(self, attrs):
        return {attr: str(getattr(self, attr)) for attr in attrs}

    def __repr__(self):
        return """<{} '{}'>""".format(self.__class__.__name__, self.id)

