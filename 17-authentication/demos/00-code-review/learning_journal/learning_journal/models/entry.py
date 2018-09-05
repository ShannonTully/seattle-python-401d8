# NOTE: Made significant changes here

from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
)

from .meta import Base


class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False, unique=True)
    author = Column(Text)
    body = Column(Text)
    date = Column(DateTime)


Index('entry_index', Entry.id, unique=True, mysql_length=255)
