import os
import requests
from dotenv import load_dotenv

load_dotenv()
FILTERING = "Paris"
URL = "https://api.weatherapi.com/v1/current.json?"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    if not API_KEY:
        raise ValueError("API_KEY is missing.")
    weather_data = requests.get(
        url=URL,
        params={
            "key": API_KEY,
            "q": FILTERING,
            "lang": "en"
        }
    ).json()

    location = (
        f"{weather_data["location"]["name"]}"
        f"/{weather_data["location"]["country"]}"
    )
    date = weather_data["current"]["last_updated"]
    temp_c = weather_data["current"]["temp_c"]
    condition = weather_data["current"]["condition"]["text"]

    print(f"Performing request to Weather API for city {FILTERING}...")
    print(location, date, "Weather:", temp_c, "Celsius", condition)


if __name__ == "__main__":
    get_weather()
