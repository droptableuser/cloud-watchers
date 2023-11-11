from sqlalchemy import Column, String, Text, event, Float
from datetime import datetime
from cloudwatch.models import BaseModel
from cloudwatch.utils import db
from sqlalchemy_utils import UUIDType
from cloudwatch.models.vendors import Vendor

class SRV(BaseModel):
    __tablename__ = 'srvs'

    srv_id = Column(String(36), primary_key=True)
    vendor = Column(String(120), nullable=False)
    description = Column(Text, nullable=False)
    link = Column(String(255))
    reporter = Column(String(255), nullable=True)
    vendor_id = db.Column(UUIDType(binary=False), db.ForeignKey("vendors.id"))
    vendor = db.relationship('Vendor', backref=db.backref('srvs', lazy=True))   
    rating = Column(Float(precision=2),nullable=False)
    rating_description = Column(Text, nullable=False)

    def __init__(self,srv_id, vendor, description, link, reporter,rating, rating_description):
        self.srv_id = srv_id
        self.vendor = vendor
        self.description = description
        self.link = link
        self.reporter = reporter
        self.rating = rating
        self.rating_description = rating_description

    def generate_srv_id(self):
        current_year = datetime.now().year
        last_srv = SRV.query.filter(SRV.srv_id.like(f'SRV-{current_year}-%')).order_by(SRV.srv_id.desc()).first()
        if last_srv:
            last_id = int(last_srv.srv_id.split('-')[-1])
            new_id = last_id + 1
        else:
            new_id = 1
        return f"SRV-{current_year}-{str(new_id).zfill(4)}"

    def __repr__(self):
        return f'<SRV {self.srv_id}>'

# SQL Alchemy event listener to ensure the srv_id is generated before insert
@event.listens_for(SRV, 'before_insert')
def receive_before_insert(mapper, connection, target):
    if not target.srv_id:
        target.srv_id = target.generate_srv_id()
