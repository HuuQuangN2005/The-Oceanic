from oceanic.models.base import BaseModel
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String,UUID, Integer, ForeignKey

from flask_login import UserMixin
from uuid import uuid4

from oceanic import app
from oceanic.models import db

class UserRole(BaseModel):
    __tablename__ = "user_roles"
    name =  Column(String(50), unique=True)
    
    def __str__(self):
        return f"<<id: {self.id} name: {self.name}>>"
 
class UserDescription(BaseModel):
    __tablename__ = "user_descriptions"
    
    account = relationship('Account', backref='description', lazy=True)
    first_name = Column(String(50),nullable=False)
    last_name =  Column(String(50),nullable=False)
    
    
    
class Account(BaseModel, UserMixin):
    __tablename__ = "user_accounts"
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    
    #uuid = Column(UUID,unique=True,default=uuid4)
    
    description_id = Column(Integer, ForeignKey(UserDescription.id),nullable=False, unique=True )
    role_id = Column(Integer,ForeignKey(UserRole.id), nullable=False, unique=True)
    
    
class PhoneNumber(BaseModel):
    __tablename__ = "user_phonenumbers"
    phonenumber = Column(String(12),nullable=True)


if __name__ == '__main__':
    with app.app_context():
       db.create_all() 
