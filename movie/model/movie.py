from config.configDatabase import Base
from sqlalchemy import Integer, String, Float, Column, ForeignKey
from sqlalchemy.orm import relationship


class Movie(Base):
    __tablename__ = 'movie'
    __table_args__ = {'schema': 'main'}

    movie_id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    title = Column(String, nullable=False)
    overview = Column(String, nullable=False)
    year = Column(String, nullable=False)
    rating = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey('main.category.category_id'), nullable=False)
    category = relationship('Category', back_populates='movies')
