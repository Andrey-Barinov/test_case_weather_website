import requests
from requests import Response
from weather_website.coords_of_city import get_coords_of_city_by_name
from weather_website.weather_data_parser import parse_weather_data


def get_weather_for_next_24_hours(city):
    """
    Function gets weather data from open-meteo api and
    returns split weather data
    If coords is None or TimeoutError function returns None
    """
    coords = get_coords_of_city_by_name(city)

    if coords is None:
        return None

    try:
        weather_data: Response = requests.get(
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={coords['lat']}&longitude={coords['lon']}&"
            f"forecast_days=1&forecast_hours=12&"
            f"hourly=temperature_2m&timezone=auto",
            timeout=15
        )
    except TimeoutError:
        return None

    split_weather_data = parse_weather_data(weather_data.json())

    return split_weather_data
