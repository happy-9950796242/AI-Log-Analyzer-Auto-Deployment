from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

from app.database import Base


class Log(Base):
    _tablename_ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    level = Column(String(50))
    message = Column(Text)
    source = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)