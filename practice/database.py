from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql+psycopg://postgres:2407@127.0.0.1:5432/inventory_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)