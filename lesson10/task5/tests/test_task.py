from lesson10.task5.task import app, vocab
from lesson10.utils import SkyproTestCase


class TestCase(SkyproTestCase):
    def test_index(self):
        with app.test_client() as client:
            for key, value in vocab.items():
                resp = client.get(f'/{key}/')
                expected = f'Значение для ключа {key} - {value}'

                self.assertEqual(resp.status_code, 200,
                                 msg=f'Урл /{key}/ должен возвращать код ответа 200')
                self.assertEqual(resp.get_data(True), expected,
                                 msg=f'Урл /{key}/ должен возвращать "{expected}"')

            resp = client.get(f'/not_vacab_value/')
            expected = 'Ключ не найден'

            self.assertEqual(resp.status_code, 404,
                             msg=f'Для значений не из словаря представление должно возвращать код ответа 404')
            self.assertEqual(resp.get_data(True), expected,
                             msg=f'Для значений не из словаря представление должно возвращать "{expected}"')
