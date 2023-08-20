import requests


def create_folder(url, name_folder, headers):
    request = requests.put(f'{url}?path={name_folder}', headers=headers)
    return request.status_code