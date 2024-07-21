import os
from dotenv import load_dotenv
from flask import (
    Flask,
    render_template,
    request,
    make_response,
    get_flashed_messages,
    flash,
    redirect,
    url_for
)
from weather_website.weather_api import get_weather_for_next_24_hours

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.get('/')
def home():
    """Return homepage"""
    messages = get_flashed_messages(with_categories=True)
    response = make_response(render_template('index.html', messages=messages))
    return response


@app.post('/')
def get_weather():
    """Return homepage with the weather or with flash message with error"""
    city = request.form.get('city')
    weather = get_weather_for_next_24_hours(city)
    if weather is None:
        flash(
            'Некорректно введено название города или сервер не отвечает, '
            'пожалуйста, повторите попытку позже',
            'warning'
        )
        return redirect(url_for('home'))

    return render_template('index.html', weather=weather, city=city)
