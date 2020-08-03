from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from utils import add_to_db

engine = create_engine('sqlite:///mnbipoc.db', echo=True)
Base = declarative_base()

class MNBIPOC(Base):
    """"""
    __tablename__ = "mnbipoc"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    clinic = Column(String)
    website = Column(String)
    email = Column(String)
    phone = Column(Integer)
    race = Column(String)
    language = Column(String)
    services = Column(String)

# create tables
Base.metadata.create_all(engine)

add_to_db("mnxl.xlsx")
