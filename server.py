from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db_wrapper import get_db, RecordRepository
from requests_models import DataInput
from service import RecordService
from fastapi.responses import PlainTextResponse

app = FastAPI()


def get_service(db: Session = Depends(get_db)):
    repository = RecordRepository(db)
    return RecordService(repository)


@app.post("/data")
async def receive_data(
    data_from_request: DataInput,
    service: RecordService = Depends(get_service)
):
    response_text = service.process_data(data_from_request.data)
    return PlainTextResponse(content=response_text)


@app.get("/showall")
async def show_all(service: RecordService = Depends(get_service)):
    records = service.get_all_records()
    return records
