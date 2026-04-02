from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
from enum import Enum

# --- ENUMS (Strict choices) ---


class RoleEnum(str, Enum):
    VIEWER = "VIEWER"
    ANALYST = "ANALYST"
    ADMIN = "ADMIN"


class TransactionType(str, Enum):
    INCOME = "INCOME"
    EXPENSE = "EXPENSE"

# --- USER SCHEMAS ---


class UserBase(BaseModel):
    email: EmailStr
    role: RoleEnum = RoleEnum.VIEWER


class UserCreate(UserBase):
    password: str = Field(..., min_length=8,
                          description="Password must be at least 8 characters")


class UserResponse(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True  # This tells Pydantic to read data from our database models later

# --- RECORD SCHEMAS ---


class RecordBase(BaseModel):
    amount: float = Field(..., gt=0,
                          description="Amount must be greater than 0")
    type: TransactionType
    category: str
    date: datetime
    notes: Optional[str] = None


class RecordCreate(RecordBase):
    pass  # We just need the base fields to create a record


class RecordResponse(RecordBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True

# For Updating: All fields are optional so you can update just one thing


class RecordUpdate(BaseModel):
    amount: Optional[float] = None
    type: Optional[TransactionType] = None
    category: Optional[str] = None
    date: Optional[datetime] = None
    notes: Optional[str] = None

# For the Dashboard


class CategoryTotal(BaseModel):
    category: str
    total: float
