def parse_weather_data(data):
    """
    Function parses the data received from open-meteo api and splits date+time
    """
    split_date_time = map(lambda x: x.split('T'), data['hourly']['time'])
    weather = zip(split_date_time, data['hourly']['temperature_2m'])

    return list(weather)
