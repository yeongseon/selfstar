from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from ..core.config import get_settings

settings = get_settings()
engine = create_async_engine(settings.async_database_url, echo=settings.DB_ECHO, pool_pre_ping=True)

AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
