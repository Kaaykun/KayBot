import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    weather_api_key = os.environ.get('WEATHER_API_KEY') or 'get-your-own-key'
    news_api_key = os.environ.get('NEWS_API_KEY') or 'get-your-own-key'
