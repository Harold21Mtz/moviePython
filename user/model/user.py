from sqlalchemy import String, Column, Integer
from config.configDatabase import Base


class User(Base):
    __tablename__ = "user"
    __table_args__ = {"schema": "main"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=True)
