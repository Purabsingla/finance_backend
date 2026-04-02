from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey, Boolean, Enum
from sqlalchemy.orm import relationship
from .database import Base
import datetime
from .schemas import RoleEnum, TransactionType


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String, default=RoleEnum.VIEWER)
    is_active = Column(Boolean, default=True)

    records = relationship("Record", back_populates="owner")


class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    type = Column(String)  # INCOME or EXPENSE
    category = Column(String)
    date = Column(DateTime)
    notes = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="records")
