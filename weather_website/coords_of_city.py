from geopy.geocoders import Nominatim


def get_coords_of_city_by_name(name_of_city):

    """Function create a dict with latitude and longitude coordinates.
    Works with RU and ENG languages. Adds the missing part of the letters.
    If wrong name of the city return None"""
    geolocator = Nominatim(user_agent="City")
    city = geolocator.geocode(name_of_city)

    if city is None:
        return None

    city_lat = city.latitude
    city_lon = city.longitude

    return {'lat': city_lat, 'lon': city_lon}
