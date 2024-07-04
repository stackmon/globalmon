import unittest
from unittest.mock import patch
from globalmon.utils import heartbeat_check


class TestHeartbeatCheck(unittest.TestCase):

    @patch('globalmon.utils.requests.get')
    def test_heartbeat_check_success(self, mock_get):
        mock_get.return_value.status_code = 200
        services = {
            'example_service': {'urls': ['https://example.com']}
        }
        result = heartbeat_check(services)
        expected_result = {
            'example_service': {
                # Expected response time
                'https://example.com': {'return_code': 200, 'return_time': 0}
            }
        }
        self.assertEqual(result, expected_result)

    @patch('globalmon.utils.requests.get')
    def test_heartbeat_check_failure(self, mock_get):
        mock_get.side_effect = Exception("Connection Error")
        services = {
            'example_service': {'urls': ['https://example.com']}
        }
        with self.assertRaises(Exception) as context:
            heartbeat_check(services)

        self.assertEqual(str(context.exception), "Connection Error")


if __name__ == '__main__':
    unittest.main()
