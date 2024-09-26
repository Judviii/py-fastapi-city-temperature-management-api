import httpx
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")


async def fetch_city_temperature(city_name: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric"
        )
        data = response.json()
        return data["main"]["temp"] if response.status_code == 200 else None
