import db
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

class Customer():
    __tablename__ = "Customer"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)