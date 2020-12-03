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
    def create_bear_with_specified_parameter(**kwargs):
        path = '/bear'
        param_name = next(iter(kwargs))
        if param_name == 'bear_name':
            data = Bear(bear_name=kwargs[param_name])
        elif param_name == 'bear_type':
            data = Bear(bear_type=kwargs[param_name])
        elif param_name == 'bear_age':
            data = Bear(bear_age=kwargs[param_name])
        else:
            raise Exception("Invalid parameter")

        response = requests.post(url + path, data=json.dumps(data.__dict__), headers=headers)
        return response

    """Updating bear"""

    @staticmethod
    def update_bear_with_specified_parameter(bear_id, **kwargs):
        path = f'/bear/{bear_id}'
        response = requests.put(url + path, data=json.dumps(kwargs), headers=headers)
        return response

    """Deleting bear"""

    @staticmethod
    def delete_bear_by_id(bear_id):
        path = f'/bear/{bear_id}'
        response = requests.delete(url + path, headers=headers)
        return response
