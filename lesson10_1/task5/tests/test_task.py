from lesson10_1.task5.task import app
from lesson10_1.utils import SkyproTestCase


class TestCase(SkyproTestCase):
    def test_sort(self):
        with app.test_client() as client:
            resp = client.get('/sort/')
            self.assertNotEqual(404, resp.status_code, msg='Представление должно работать по урлу /sort/')

            resp = client.get('/sort/?key=first_name&direction=desc')
            self.assertNotEqual(400, resp.status_code, msg='Представление должно принимать параметры key и direction')

            resp = client.get('/sort/?key=first_name&direction=desc')
            expected = 'Larsen Solis'

            self.assertEqual(expected, resp.get_data(True),
                             msg=f'При сортировке по first_name по убыванию первым в списке должен быть {expected}')

            resp = client.get('/sort/?key=last_name&direction=desc')
            expected = 'Wong Gordon'

            self.assertEqual(expected, resp.get_data(True),
                             msg=f'При сортировке по last_name по убыванию первым в списке должен быть {expected}')

            resp = client.get('/sort/?key=last_name&direction=asc')
            expected = 'Battle Hester'

            self.assertEqual(expected, resp.get_data(True),
                             msg=f'При сортировке по last_name по возрастанию первым в списке должен быть {expected}')

            resp = client.get('/sort/?key=first_name&direction=asc')
            expected = 'Rivers Castaneda'

            self.assertEqual(expected, resp.get_data(True),
                             msg=f'При сортировке по first_name по возрастанию первым в списке должен быть {expected}')
