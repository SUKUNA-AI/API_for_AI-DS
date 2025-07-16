"""
Настраивает SQLAlchemy для использования базы данных PostgresSQL
"""

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:qwerty12345@localhost:5432/fantasy_data"
engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, class_=AsyncSession)

Base = declarative_base()