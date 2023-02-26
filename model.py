from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from db_handler import Base
import sqlalchemy.orm as orm


class User(Base):

    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    user_id = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, index=True, nullable=False)
    email = Column(String, index=True, nullable=False)
    cpf = Column(String, index=True, nullable=False)
    pis = Column(String, index=True, nullable=False)
    password = Column(String, index=True, nullable=False)
    country = Column(String, index=True, nullable=False)
    state = Column(String, index=True, nullable=False)
    city = Column(String, index=True, nullable=False)
    street = Column(String, index=True, nullable=False)
    number = Column(Integer, index=True, nullable=False)
    complement = Column(String, index=True, nullable=False)
