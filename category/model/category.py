from config.configDatabase import Base
from sqlalchemy import String, Integer, Column
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = "category"
    __table_args__ = {'schema': 'main'}

    category_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    category_name = Column(String, unique=True, nullable=False)
    category_description = Column(String, nullable=False)
    movies = relationship("Movie", back_populates="category")
