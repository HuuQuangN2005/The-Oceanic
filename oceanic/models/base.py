from oceanic.models import db
from sqlalchemy import Column, Integer,DateTime, Boolean
from datetime import datetime


class BaseModel(db.Model):
    __abstract__ = True
    
    id = Column(Integer,autoincrement=True,primary_key=True)
    created_date = Column(DateTime,default=datetime.now)
    active = Column(Boolean, default=True)
    