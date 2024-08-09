from sqlalchemy import create_engine, Column, Integer, String, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings

Base = declarative_base()


class RecordEntity(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True)
    bib_number = Column(String, index=True)
    channel_id = Column(String)
    timestamp = Column(Time)
    group_number = Column(String)


engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class RecordRepository:
    def __init__(self, db):
        self.db = db

    def add_record(self, bib_number: str, channel_id: str, timestamp, group_number: str):
        db_record = RecordEntity(
            bib_number=bib_number,
            channel_id=channel_id,
            timestamp=timestamp,
            group_number=group_number
        )
        self.db.add(db_record)
        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def get_all_records(self):
        return self.db.query(RecordEntity).all()
