#!python3
"""
inkycal_weather unittest
"""
import logging
import sys
import unittest
from inkycal.modules import Weather as Module

from inkycal.modules.inky_image import Inkyimage
from inkycal.tests import Config
preview = Inkyimage.preview
merge = Inkyimage.merge

owm_api_key = Config.OPENWEATHERMAP_API_KEY
location = 'Stuttgart, DE'

tests = [
    {
        "position": 1,
        "name": "Weather",
        "config": {
            "size": [500, 100],
            "api_key": owm_api_key,
            "location": location,
            "round_temperature": True,
            "round_windspeed": True,
            "forecast_interval": "daily",
            "units": "metric",
            "hour_format": "12",
            "use_beaufort": True,
            "padding_x": 10,
            "padding_y": 10,
            "fontsize": 12,
            "language": "en"
        }
    },
    {
        "position": 1,
        "name": "Weather",
        "config": {
            "size": [500, 150],
            "api_key": owm_api_key,
            "location": "2643123",
            "round_temperature": True,
            "round_windspeed": True,
            "forecast_interval": "daily",
            "units": "metric",
            "hour_format": "12",
            "use_beaufort": True,
            "padding_x": 10,
            "padding_y": 10,
            "fontsize": 12,
            "language": "en"
        }
    },
    {
        "position": 1,
        "name": "Weather",
        "config": {
            "size": [500, 200],
            "api_key": owm_api_key,
            "location": location,
            "round_temperature": False,
            "round_windspeed": True,
            "forecast_interval": "daily",
            "units": "metric",
            "hour_format": "12",
            "use_beaufort": True,
            "padding_x": 10,
            "padding_y": 10,
            "fontsize": 12,
            "language": "en"
        }
    },
    {
        "position": 1,
        "name": "Weather",
        "config": {
            "size": [500, 100],
            "api_key": owm_api_key,
            "location": location,
            "round_temperature": True,
            "round_windspeed": False,
            "forecast_interval": "daily",
            "units": "metric",
            "hour_format": "12",
            "use_beaufort": True,
            "padding_x": 10,
            "padding_y": 10,
            "fontsize": 12,
            "language": "en"
        }
    },
    {
        "position": 1,
        "name": "Weather",
        "config": {
            "size": [500, 150],
            "api_key": owm_api_key,
            "location": location,
            "round_temperature": True,
            "round_windspeed": True,
            "forecast_interval": "hourly",
            "units": "metric",
            "hour_format": "12",
            "use_beaufort": True,
            "padding_x": 10,
            "padding_y": 10,
            "fontsize": 12,
            "language": "en"
        }
    },
    {
        "position": 1,
        "name": "Weather",
        "config": {
            "size": [500, 150],
            "api_key": owm_api_key,
            "location": location,
            "round_temperature": True,
            "round_windspeed": True,
            "forecast_interval": "daily",
            "units": "imperial",
            "hour_format": "12",
            "use_beaufort": True,
            "padding_x": 10,
            "padding_y": 10,
            "fontsize": 12,
            "language": "en"
        }
    },
    {
        "position": 1,
        "name": "Weather",
        "config": {
            "size": [500, 100],
            "api_key": owm_api_key,
            "location": location,
            "round_temperature": True,
            "round_windspeed": True,
            "forecast_interval": "daily",
            "units": "metric",
            "hour_format": "24",
            "use_beaufort": True,
            "padding_x": 10,
            "padding_y": 10,
            "fontsize": 12,
            "language": "en"
        }
    },
    {
        "position": 1,
        "name": "Weather",
        "config": {
            "size": [500, 100],
            "api_key": owm_api_key,
            "location": location,
            "round_temperature": True,
            "round_windspeed": True,
            "forecast_interval": "daily",
            "units": "metric",
            "hour_format": "12",
            "use_beaufort": False,
            "padding_x": 10,
            "padding_y": 10,
            "fontsize": 12,
            "language": "en"
        }
    },
]


class module_test(unittest.TestCase):
    def test_get_config(self):
        print('getting data for web-ui...', end="")
        Module.get_config()
        print('OK')

    def test_generate_image(self):
        for test in tests:
            print(f'test {tests.index(test) + 1} generating image..')
            module = Module(test)
            im_black, im_colour = module.generate_image()
            print('OK')
            if Config.USE_PREVIEW:
                preview(merge(im_black, im_colour))



if __name__ == '__main__':
    logger = logging.getLogger()
    logger.level = logging.DEBUG
    logger.addHandler(logging.StreamHandler(sys.stdout))

    unittest.main()
