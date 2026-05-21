from datetime import datetime, UTC
from uuid import uuid4

def generate_uuid() -> str:
    return str(uuid4())

def get_current_timestamp() -> str:
    return datetime.now(UTC).isoformat()

def format_datetime(value: datetime) -> str:
    return value.strftime("%Y-%m-%d %H:%M:%S")