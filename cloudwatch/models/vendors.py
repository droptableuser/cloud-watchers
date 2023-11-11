from cloudwatch.models import BaseModel
from sqlalchemy import Column, String


class Vendor(BaseModel):
    __tablename__ = 'vendors'

    name = Column(String(120), nullable=False, unique=True)
    vendor_type = Column(String(120), nullable=False)

    def __repr__(self):
        return f'<Vendor {self.name}>'