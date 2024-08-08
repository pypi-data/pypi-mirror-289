import unittest
from unittest.mock import patch
from pyTuxAPI.api_client import TuxAPIClient

class TestTuxAPIClient(unittest.TestCase):
    @patch('pyTuxAPI.api_client.requests.get')
    def test_get_data(self, mock_get):
        mock_get.return_value.ok = True
        mock_get.return_value.json.return_value = {'key': 'value'}

        client = TuxAPIClient('http://api.example.com', 'fake_api_key')
        result = client.get_data('test-endpoint')

        self.assertEqual(result, {'key': 'value'})
        mock_get.assert_called_once_with(
            'http://api.example.com/test-endpoint',
            headers={'Authorization': 'Bearer fake_api_key'}
        )

if __name__ == '__main__':
    unittest.main()
