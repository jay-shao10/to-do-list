from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, Boolean, DateTime, Integer, create_engine
from datetime import datetime
from dotenv import load_dotenv
import os
# import crud_item
# import create_db

load_dotenv()
db_pwd = os.environ.get('DB_PASSWORD')
db_user = os.environ.get('DB_USER')
db_database = os.environ.get('DB_DATABASE')
connection_str = f"postgresql+psycopg2://{db_user}:{db_pwd}@localhost/{db_database}"
# print(connection_str)

Base = declarative_base()
engine = create_engine(connection_str, echo=False)
Session = sessionmaker()
"""
class Item
id int
itemname str
isFinish str
date_created datetime

"""

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer(), primary_key=True)
    item_name = Column(String(25), nullable=False, unique=True)
    is_finish = Column(Boolean(),nullable=False, default=False)
    date_created = Column(DateTime(), default=datetime.utcnow)




