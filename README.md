### Hexlet tests and linter status:
[![Python CI](https://github.com/Andrey-Barinov/test_case_weather_website/actions/workflows/pyci.yaml/badge.svg)](https://github.com/Andrey-Barinov/test_case_weather_website/actions/workflows/pyci.yaml)
[![Maintainability](https://api.codeclimate.com/v1/badges/496e496606fa08fff34f/maintainability)](https://codeclimate.com/github/Andrey-Barinov/test_case_weather_website/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/496e496606fa08fff34f/test_coverage)](https://codeclimate.com/github/Andrey-Barinov/test_case_weather_website/test_coverage)

<h1>Тестовое задание Python Developer </h1>
Сделать web приложение, оно же сайт, где пользователь вводит название города, и получает прогноз погоды в этом городе на ближайшее время.

 - *Вывод данных (прогноза погоды) должен быть в удобно читаемом формате. (Выполнено) 

 - Веб фреймворк можно использовать любой. (Выполнено) 

 - api для погоды:* https://open-meteo.com/ *(можно использовать какое-нибудь другое, если вам удобнее)* (Выполнено) 

будет плюсом если:

- написаны тесты (Выполнено)
  
<b>Использовал микрофреймвоорк Flask, публичную библеотеку geopy для получения координатов городов и pytest для тестировния.</b>
  
<b>Требования:</b>
1. Python >=3.10
2. poetry >= 1.6.1
3. flask >= 3.0.3 flask

<b>Установка:</b>
1. Клонировать репозиторий: `git@https://github.com/Andrey-Barinov/test_case_weather_website.git`
2. Перейти в директорию: `cd test_case_weather_website`
3. Настроить poetry для создания виртуальной среды: `poetry config virtualenvs.in-project true`
4. Создать виртуальное окружение и установить зависимости: `make install`
5. Создать файл в формате `.env` в корневой директории по примеру `.env_example` файла этого репозитория.
6. Запусить приложение режиме разработки: `make dev`
