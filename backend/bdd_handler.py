from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import StockData
import yfinance as yf

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://finance:finance@db/finance"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def fetch_stock_data_and_insert():
    try:
        db = SessionLocal()
        stock_data = yf.download('AAPL', start='2023-01-12', end='2023-05-12')

        for index, row in stock_data.iterrows():
            db.add(StockData(
                date=index.strftime('%Y-%m-%d'),
                open=row['Open'],
                high=row['High'],
                low=row['Low'],
                close=row['Close'],
                volume=row['Volume'],
                ticker='AAPL'
            ))

        db.commit()
        print("Data inserted into PostgreSQL.")

    except Exception as e:
        print("Error inserting data:", e)

    finally:
        db.close()
