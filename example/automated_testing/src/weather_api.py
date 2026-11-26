import requests


def get_weather(city: str) -> dict:
    response = requests.get(
        "https://example.com/weather",
        params={"city": city},
        timeout=30,
    )

    response.raise_for_status()

    return response.json()
