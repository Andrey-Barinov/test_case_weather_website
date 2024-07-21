import pytest
from weather_website import app
from weather_website.coords_of_city import get_coords_of_city_by_name
from weather_website.weather_data_parser import parse_weather_data


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_get_home(client):
    response = client.get('/')
    assert response.status_code == 200


def test_page_not_found(client):
    response = client.get('/something')
    assert response.status_code == 404


def test_post_url_with_right_name_of_city(client):
    response = client.post('/', data={'city': 'Москва'})

    assert response.status_code == 200
    assert 'Москва' in response.get_data(as_text=True)
    assert 'Дата' in response.get_data(as_text=True)
    assert 'Время' in response.get_data(as_text=True)
    assert 'Температура' in response.get_data(as_text=True)


def test_post_url_with_wrong_name_of_city(client):
    response = client.post('/', data={'city': 'dasdasfas'})
    assert response.status_code == 302


def test_get_coords_of_city_by_name():
    coord_with_right_name = get_coords_of_city_by_name('Москва')
    right_coords = {'lat': 55.625578, 'lon': 37.6063916}

    assert coord_with_right_name == right_coords

    coord_with_wrong_name = get_coords_of_city_by_name('dasdasfas')

    assert coord_with_wrong_name is None


data_from_open_meteo = {
    'latitude': 55.75,
    'longitude': 37.625,
    'generationtime_ms': 0.02288818359375,
    'utc_offset_seconds': 10800, 'timezone': 'Europe/Moscow',
    'timezone_abbreviation': 'MSK',
    'elevation': 157.0,
    'hourly_units': {'time': 'iso8601', 'temperature_2m': '°C'},
    'hourly': {
        'time': ['2024-07-20T16:00', '2024-07-20T17:00'],
        'temperature_2m': [23.9, 23.4]}
}

right_split_data = [(['2024-07-20', '16:00'], 23.9), (['2024-07-20', '17:00'], 23.4)]


def test_parser_weather_data():
    parser_weather_data = parse_weather_data(data_from_open_meteo)

    assert parser_weather_data == right_split_data
