from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from .database import Base
from datetime import datetime
from sqlalchemy.sql import func

class Word(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True, index=True)
    french_word = Column(String, index=True, unique=True, nullable=False)
    translation = Column(String, nullable=False)

    level = Column(Integer, default=1)
    correct_streak = Column(Integer, default=0)

    time_seen = Column(Integer, default=0)
    times_correct = Column(Integer, default=0)

    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Stats(Base):
    __tablename__ = "stats"

    id = Column(Integer, primary_key=True, index=True)
    xp_total = Column(Integer, default=0)
    sessions_completed = Column(Integer, default=0)
    total_correct = Column(Integer, default=0)
    total_wrong = Column(Integer, default=0)