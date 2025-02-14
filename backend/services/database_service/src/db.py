from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.common.config import DATABASE_URL

db_engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)