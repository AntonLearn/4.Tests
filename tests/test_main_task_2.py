import pytest
from main_task_2 import create_folder


@pytest.mark.parametrize(
    'name_folder, expected',
    [
        ('New Folder 1', 201),
        ('New Folder 2', 201),
        ('New Folder 3', 201)
    ]
)
def test_create_folder(name_folder, expected):
    with open('params.txt', 'r', encoding='utf-8') as file:
        token = file.readline().rstrip()
        url = file.readline().rstrip()
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
    result = create_folder(url, name_folder, headers)
    err_dict = {
        400: f'Некорректные данные!',
        401: f'Не авторизован!',
        403: f'API недоступно. Ваши файлы занимают больше места, чем у вас есть. Удалите лишнее или увеличьте объём Диска!',
        404: f'Не удалось найти запрошенный ресурс!',
        406: f'Ресурс не может быть представлен в запрошенном формате!',
        409: f'Папка {name_folder} уже существует!',
        413: f'Загрузка файла недоступна. Файл слишком большой!',
        423: f'Технические работы. Сейчас можно только просматривать и скачивать файлы!',
        429: f'Слишком много запросов!',
        503: f'Сервис временно недоступен!',
        507: f'Недостаточно свободного места!'
    }
    err_message = err_dict.get(result, f'Ошибка создания папки {name_folder}!')
    assert result == expected, err_message



