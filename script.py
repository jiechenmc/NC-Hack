import requests
import os
from dotenv import load_dotenv
from pathlib import Path
from pyzipcode import ZipCodeDatabase

zcdb = ZipCodeDatabase()
load_dotenv()
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


def get_weather_condition(zip_code, country_code="us"):
    try:
        api_key = os.getenv("weather_api_key")
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code},{country_code}&appid={api_key}"
        ).json()
        return r["weather"][0]["main"].lower()
    except KeyError:
        # There is no weather data for the zip code
        pass


def make_markers(*zip_codes):
    marker = "color:blue%7Clabel:S%7C"
    runs = 0
    for zip_code in zip_codes:
        if runs != 0:
            marker += f"|{zip_code}"
        else:
            marker += str(zip_code)
            runs += 1
    return marker


def get_nearby_zip(zip_code):
    in_radius = (z.zip for z in zcdb.get_zipcodes_around_radius(zip_code, 8))
    return in_radius


def get_map_link(zip_code):
    api_key = os.getenv("map_api_key")
    home_marker = f"color:red%7Clabel:H%7C{zip_code}"
    snow_zips = [
        code for code in get_nearby_zip(zip_code)
        if get_weather_condition(code) == "snow"
    ]

    marker = make_markers(*snow_zips)
    map_link = f"https://maps.googleapis.com/maps/api/staticmap?center={zip_code}&zoom=10&size=640x640&maptype=roadmap&markers={home_marker}&markers={marker}&key={api_key}"
    return map_link