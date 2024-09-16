import unittest
from app import create_app

class ItemRoutesTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_item(self):
        response = self.client.post('/items', json={'name': 'Item 3', 'description': 'Description for Item 3'})
        self.assertEqual(response.status_code, 201)

    def test_get_items(self):
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
