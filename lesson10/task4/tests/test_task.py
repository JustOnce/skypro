import unittest

from lesson10.task4.task import app
from lesson10.task4.users import users
from lesson10.utils import SkyproTestCase


class TestCase(SkyproTestCase):
    def test_users(self):
        with app.test_client() as client:
            resp = client.get('/users/1/')
            self.assertNotEqual(resp.status_code, 404, msg='Представление должно работать по урлу /users/1/')

            resp = client.get('/users/fsdfsd/')
            self.assertEqual(resp.status_code, 404,
                             msg='Представление должно обрабатывать сегмент урла как целое число')

            not_found_str = 'Не найдено'

            for i in (0, 11, 20, 100, 1000):
                resp = client.get(f'/users/{i}/')

                self.assertEqual(resp.status_code, 404,
                                 msg=f'Если по индексу не найден пользователь, то код ответ должен быть 404')
                self.assertEqual(resp.get_data(True), not_found_str,
                                 msg=f'Если по индексу не найден пользователь, то ответ должен быть {not_found_str}')

            for i, user in enumerate(users, start=1):
                resp = client.get(f'/users/{i}/')
                expected = f'{user["last_name"]} {user["first_name"]}'

                self.assertEqual(resp.status_code, 200,
                                 msg=f'По индексу {i} должен возвращаться код ответа 200')
                self.assertEqual(resp.get_data(True), expected,
                                 msg=f'По индексу {i} должен возвращаться ответ {expected}')
