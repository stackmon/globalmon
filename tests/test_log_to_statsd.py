import unittest
from unittest.mock import MagicMock, patch
from globalmon.utils import log_to_statsd


class TestLogToStatsd(unittest.TestCase):

    @patch('globalmon.utils.statsd.StatsClient')
    def test_log_to_statsd(self, mock_stats_client):
        mock_client = MagicMock()
        mock_stats_client.return_value = mock_client
        results = {
            'example_service': {
                'http://example.com': {"return_code": 200, "return_time": 100}
            }
        }
        log_to_statsd(mock_client, 'prefix', results)
        mock_client.timing.assert_called_once_with(
            'prefix.example_service.example_com.200', 100)
        # Verify both increment calls
        mock_client.incr.assert_has_calls([
            # First increment call with the return code
            unittest.mock.call('counter.prefix.example_service.example_com.200'),
            # Second increment call for 'attempted'
            unittest.mock.call('counter.prefix.example_service.example_com.attempted')
        ], any_order=True)


if __name__ == '__main__':
    unittest.main()
