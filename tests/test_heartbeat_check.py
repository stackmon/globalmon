import unittest
from unittest.mock import patch
import requests
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
                'https://example.com': {'return_code': 200, 'return_time': 0}
            }
        }
        self.assertEqual(result, expected_result)

    @patch('globalmon.utils.requests.get')
    def test_heartbeat_check_timeout(self, mock_get):
        mock_get.side_effect = requests.exceptions.Timeout
        services = {
            'example_service': {
                'urls': ['https://example.com']
                }
        }
        result = heartbeat_check(services)
        expected_result = {'example_service': {
            'https://example.com': {
                'return_code': 'timeout', 'return_time': 10000
                }
            }
        }
        self.assertEqual(result, expected_result)

    @patch('globalmon.utils.requests.get')
    def test_heartbeat_check_failure(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException(
            "Connection Error")
        services = {
            'example_service': {
                'urls': ['https://example.com']
            }
        }
        result = heartbeat_check(services)
        expected_result = {'example_service': {
            'https://example.com': {
                'return_code': 'failed', 'return_time': 0
                }
            }
        }
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
