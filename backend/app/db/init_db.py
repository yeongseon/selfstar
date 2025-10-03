import asyncio
from sqlalchemy.exc import OperationalError
from .session import engine
from ..models import Base

async def init_db(retries: int = 5, initial_delay: float = 0.8) -> None:
    """Initialize database (dev only): create tables with simple retry/backoff.

    Retries help when the app starts faster than the MySQL container.
    """
    delay = initial_delay
    for attempt in range(1, retries + 1):
        try:
            async with engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
            return
        except OperationalError as e:  # pragma: no cover - transient startup path
            if attempt == retries:
                raise
            await asyncio.sleep(delay)
            delay *= 1.6
