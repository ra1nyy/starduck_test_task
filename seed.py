from sqlalchemy.orm import Session
from db_wrapper import RecordEntity, engine, Base
from datetime import time

Base.metadata.create_all(bind=engine)


def seed_data(db: Session):
    # Пример данных для сидинга
    test_records = [
        RecordEntity(bib_number="0001", channel_id="C1", timestamp=time(1, 10, 20), group_number="00"),
        RecordEntity(bib_number="0002", channel_id="C2", timestamp=time(1, 12, 30), group_number="00"),
        RecordEntity(bib_number="0003", channel_id="C1", timestamp=time(1, 15, 45), group_number="01"),
        RecordEntity(bib_number="0004", channel_id="C2", timestamp=time(1, 18, 50), group_number="00"),
        RecordEntity(bib_number="0005", channel_id="C3", timestamp=time(1, 20, 10), group_number="02"),
    ]
    db.add_all(test_records)
    db.commit()
    print("Test data seeded successfully!")


if __name__ == "__main__":
    with Session(bind=engine) as session:
        seed_data(session)
