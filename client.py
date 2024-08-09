import aiohttp
import asyncio

BASE_URL = 'http://127.0.0.1:3004'


async def send_data(data):
    async with aiohttp.ClientSession() as session:
        payload = {"data": data}
        async with session.post(f"{BASE_URL}/data", json=payload) as response:
            resp_text = await response.text()
            print(f"Send: {data}")
            print(f"Received: {resp_text}")


async def show_all():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{BASE_URL}/showall") as response:
            records = await response.json()
            print("All records:")
            for record in records:
                print(record)

if __name__ == "__main__":
    data_examples = [
        "0002 C1 01:13:02.877 00[CR]",
        "0003 C1 01:15:45.123 01[CR]",
        "0004 C1 01:17:33.456 00[CR]",
    ]

    loop = asyncio.get_event_loop()

    # Отправляем данные на сервер
    tasks = [send_data(data) for data in data_examples]
    loop.run_until_complete(asyncio.gather(*tasks))

    # Запрашиваем все данные с сервера
    loop.run_until_complete(show_all())
