from config.databaseProducts import Base
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey

class product(Base):
    __tablename__ = "Products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    units = Column(Integer, nullable=False)