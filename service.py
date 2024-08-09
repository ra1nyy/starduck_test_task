from fastapi import HTTPException, status
from datetime import datetime
import logging
import re
from db_wrapper import RecordRepository

logging.basicConfig(filename="server.log", level=logging.INFO, format="%(asctime)s - %(message)s")


class RecordService:
    def __init__(self, repository: RecordRepository):
        self.repository = repository
        self._data_pattern = re.compile(r"(\d{4}) (\S{2}) (\d{2}:\d{2}:\d{2})\.\d{3} (\d{2})")
        self._target_group_number = "00"

    def process_data(self, data: str) -> str:
        match = self._data_pattern.match(data.strip())
        if not match:
            logging.info(f"Received malformed data: {data}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid data format')

        bib_number, channel_id, time_str, group_number = match.groups()

        if group_number == self._target_group_number:
            timestamp = datetime.strptime(time_str, "%H:%M:%S").time()
            self.repository.add_record(bib_number, channel_id, timestamp, group_number)
            response_text = f"Спортсмен, нагрудный номер {bib_number} прошёл отсечку {channel_id} в {time_str}"
            logging.info(response_text)
            return response_text
        else:
            logging.info(f"Received data: {data}")
            return "Data received and logged"

    def get_all_records(self):
        return self.repository.get_all_records()
