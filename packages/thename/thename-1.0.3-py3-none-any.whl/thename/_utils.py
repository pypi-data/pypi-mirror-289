import requests

def _get_name():
    response = requests.get('https://devnull.cn/name')
    return response.json()
