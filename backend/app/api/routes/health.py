from fastapi import APIRouter
from datetime import datetime, timezone
from sqlalchemy import text
from ...db.session import engine

router = APIRouter(prefix="", tags=["health"])  # no extra prefix so it's /health


@router.get("/health")
async def health():
    db_status = "unknown"
    try:
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        db_status = "up"
    except Exception:  # pragma: no cover - lightweight best-effort probe
        db_status = "down"
    return {
        "status": "ok",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "db": db_status,
    }
