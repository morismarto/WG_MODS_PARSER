__all__ = ['get_exec_time', 'save_json', 'save_csv', 'create_csv']

from requests import Response
from typing import Callable
from time import time
from .models import Mods
import os
import json
import re
import csv


def get_exec_time(function: Callable) -> Callable:
    def wrapper():
        print('Parser is running...')
        t1 = time()
        function()
        delta = time() - t1
        print(f'Execution time is:{delta: .2f}')
    return wrapper


def save_json(mods: Mods, response: Response) -> None:
    if not os.path.exists('data_json'):
        os.mkdir('data_json')
    pattern = 'offset=\d{1,3}'
    file_name = f'data_json/mods_{re.search(pattern, response.url)[0][7:]}.json'
    with open(file=file_name, mode='w', encoding='utf=8') as file:
        json.dump(mods.model_dump(), file, ensure_ascii=False, indent=4)


def create_csv():
    if not os.path.exists('data_csv'):
        os.mkdir('data_csv')
    file_name = 'data_csv/mods.csv'
    with open(file=file_name, mode='w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(('Title', 'Version', 'Url_Address'))


def save_csv(mods: Mods, response: Response) -> None:
    file_name = 'data_csv/mods.csv'
    with open(file=file_name, mode='a', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(
            (mods.localizations[0].title, 
             mods.versions[0].version,
             mods.versions[0].download_url)
             )