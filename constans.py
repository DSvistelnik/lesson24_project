import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

QUERY = {
    'filter': 'filter',
    'map': 'map',
    'unique': 'unique',
    'sort': 'sort',
    'limit': 'limit'
}