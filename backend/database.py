from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

Base = declarative_base()
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///alici.db")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    from backend.models import Message
    Base.metadata.create_all(bind=engine)