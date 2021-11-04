
from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer)
    acc_no = Column(String(250), primary_key=True)
    name = Column(String(250), nullable=False)
    acc_type = Column(String(250), nullable=False)
    password = Column(String(250))
    balance = Column(String)


class Customers(Base):
    __tablename__ = 'customers'
    id = Column(Integer)
    cust_id = Column(String, primary_key=True)
    acc_no = Column(String,ForeignKey("users.acc_no"))


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
