from lesson10.utils import SkyproTestCase


class TestCase(SkyproTestCase):
    def test_add(self):
        self.assertEqual(1, 2, msg="adds 1 + 2 to equal 3")

    def test_test(self):
        self.assertEqual(1, 2, 'test')