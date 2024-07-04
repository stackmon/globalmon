# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License

import time
import requests
import logging
import statsd


def heartbeat_check(services):
    """
    Checks the reachability of URLs defined in dictionary 'services'
    Args:
    - services (dict)
      Structure:

      service_name:
          urls:
              - url1
              ...

    Returns:
    - Dictionary, result, containing return_code and return_time
      Structure:

      service_name:
        url1:
          return_code: x
          return_time: x
    """
    result = {}
    for service, url_list in services.items():
        logging.info(f"Checking {service}...")
        result[service] = {}
        for url in url_list['urls']:
            try:
                start_time = time.time()
                response = requests.get(url)
                end_time = time.time()
                # Convert to milliseconds
                response_time = int((end_time - start_time) * 1000)
                return_data = {
                    'return_code': response.status_code,
                    'return_time': response_time
                }
                result[service][url] = return_data
            except requests.RequestException as e:
                return_data = {
                    'return_code': 'Error',
                    'return_time': str(e)
                }
                result[service][url] = return_data
    return result


def initialize_statsd_client(host='localhost', port=8125):
    """
    Initialize the StatsD client.

    Args:
    - host (str): The hostname of the StatsD server. Default is 'localhost'.
    - port (int): The port of the StatsD server. Default is 8125.

    Returns:
    - statsd.StatsClient: The initialized StatsD client.
    """
    return statsd.StatsClient(host, port)


def log_to_statsd(statsd_client, path_prefix, results):
    """
    Send data to StatsD.

    Args:
    - statsd_client (statsd.StatsClient): The initialized StatsD client.
    - prefix (prefix): The name of the timer metric.
    - results (dict): The duration in milliseconds.

    """

    for service, service_results in results.items():
        logging.info(f"Logging {service}...")
        for url, response in service_results.items():
            service_path = f'{path_prefix}.{service}.{url}'
            statsd_client.timing(
                f'stats.timer.{service_path}.{response["return_code"]}',
                response['return_time'])
            statsd_client.incr(
                f'stats.counter.{service_path}.{response["return_code"]}')
