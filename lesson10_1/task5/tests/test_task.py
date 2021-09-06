from lesson10_1.task5.task import app
from lesson10_1.utils import SkyproTestCase


class TestCase(SkyproTestCase):
    def test_index(self):
        with app.test_client() as client:
            resp = client.get('/')
            self.assertNotEqual(404, resp.status_code, msg='Представление должно работать по урлу /')

            expected = 'Hello world'

            self.assertEqual(expected, resp.get_data(True), msg=f'Представление должно возвращать {expected}')
