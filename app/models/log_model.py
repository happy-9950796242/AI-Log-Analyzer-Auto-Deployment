from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.database.database import Base


class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)

    level = Column(String(50), nullable=False)

    message = Column(Text, nullable=False)

    source = Column(String(100))

    created_at = Column(DateTime, default=datetime.utcnow)

    filename = Column(String(255), nullable=True)

    analysis_result = Column(Text, nullable=True)