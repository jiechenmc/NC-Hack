# whereItSnows

whereItSnows is a tool that help you find places that are snowing near your zip code.

## Prerequisites

1. [Anaconda](https://www.anaconda.com/products/individual)
2. [OpenWeatherMapApiKey](https://openweathermap.org/api)
3. [GoogleMapsApiKey](https://developers.google.com/maps/documentation/javascript/get-api-key)

## Installation

###### Create a .env file in the root directory with the following content

```.env
weather_api_key={your_openweathermap_api_key}
map_api_key={your_googlemaps_api_key}
```

###### Installing and activating the environment

```bash
conda env create -f env.yml
conda activate whereItSnows
```

###### To run

```python
python app.py
```

**Visit http://127.0.0.1:5000/ to test out the project!**

## Usage

Input any zip code in the search bar and it will return a map with markers of areas that are snowing.

## License

[MIT](https://choosealicense.com/licenses/mit/)
