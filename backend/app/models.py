from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class StockData(Base):
    __tablename__ = 'stock_data'

    id = Column(Integer, primary_key=True)
    date = Column(String)
    open = Column(String)
    high = Column(String)
    low = Column(String)
    close = Column(String)
    volume = Column(String)
    ticker = Column(String)
