from typing import Optional

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from src.main.config.db_config import Base


class UserSchema(BaseModel):
    id: Optional[int]
    name: str


class User(Base):
    __table_args__ = {"schema": "PUBLIC"}
    __tablename__ = "fast_api_users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
