from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DB_URL = 'postgresql://postgres:12345@localhost/journal'

engine = create_engine(SQLALCHEMY_DB_URL, isolation_level="REPEATABLE READ")

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()
