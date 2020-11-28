from bear import Bear
import requests
import json
import yaml

headers = {'Content-Type': 'application/json'}

session = requests.Session()

config_file = 'config.yaml'

with open(config_file) as stream:
    configs = yaml.safe_load(stream)
    api_configs = configs["api"]


class Config:
    def __init__(self, **entries):
        self.__dict__.update(entries)


api = Config(**api_configs)
url = api.url


class BasicSteps:
    """Getting bear"""

    @staticmethod
    def get_bear_by_id(bear_id):
        path = f'/bear/{bear_id}'
        response = requests.get(url + path, headers=headers)
        return response

    """Creating bear"""

    @staticmethod
    def create_bear():
        path = '/bear'
        data = Bear()
        response = requests.post(url + path, data=json.dumps(data.__dict__), headers=headers)
        return response

    @staticmethod
    def create_bear_with_specified_type(bear_type):
        path = '/bear'
        data = Bear(bear_type=bear_type)
        response = requests.post(url + path, data=json.dumps(data.__dict__), headers=headers)
        return response

    @staticmethod
    def create_bear_with_specified_age(bear_age):
        path = '/bear'
        data = Bear(bear_age=bear_age)
        response = requests.post(url + path, data=json.dumps(data.__dict__), headers=headers)
        return response

    @staticmethod
    def create_bear_with_name_with_spaces(bear_name):
        path = '/bear'
        data = Bear(bear_name=bear_name)
        response = requests.post(url + path, data=json.dumps(data.__dict__), headers=headers)
        return response

    """Deleting bear"""

    @staticmethod
    def delete_bear_by_id(bear_id):
        path = f'/bear/{bear_id}'
        response = requests.delete(url + path, headers=headers)
        return response
