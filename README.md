## Дипломный проект. Задание 2: API-тесты
<hr>

## <h> Project: Stellar Burgers API</h>

## <h> Инструкция по запуску:</h>

### <h>1. Установите зависимости:</h>

> pip install -r requirements.txt</h>

### <h>2. Запустить все тесты:</h>.

> pytest -v

### <h>3. Посмотреть отчет по прогону html</h>

> allure serve allure_results


## <h3> Project files and description:</h3>

| Название                 | Содержание файла                                    |
|--------------------------|-----------------------------------------------------|
| Tests dir                | Директория с тестами                                |
| test_create_order.py     | Тесты на создание заказа                            |
| test_create_user.py      | Тесты на создание пользователя                      |
| test_data_change_user.py | Тесты на изменение данных пользователя              |
| test_receiving_orders.py | Тесты на получение заказов конеретного пользователя |
| test_user_login.py       | Тесты на авторизацию пользователя                   |
| conftest.py              | Фикстуры                                            |
| helpers.py               | Генератор данных пользователя                       |
| urls.py                  | Файл с Url и  эндпоинтами                           |
| data.py                  | Файл с body ответов                                 |
| requirements.txt         | Файл с зависимостями                                |
| allure_results.dir       | Файл с отчетами Allure                              |
