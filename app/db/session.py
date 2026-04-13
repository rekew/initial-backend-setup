# Python and Third party modules
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

# Project modules
from app.core.config import settings

engine = create_async_engine(settings.DATABASE_URL, echo=True)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)
