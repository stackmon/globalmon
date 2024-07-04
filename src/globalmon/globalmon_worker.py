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

import logging
import time
from globalmon.utils import (
    heartbeat_check,
    initialize_statsd_client,
    log_to_statsd,
)


class GlobalmonWorker:
    def __init__(self, config) -> None:
        self.config = config
        self.keep_running = True
        if 'statsd' in config:
            self.statsd_client = initialize_statsd_client(
                config["statsd"]["host"], config["statsd"]["port"])

    def run(self):
        """
        Starts endpoint monitoring and data collection.
        """
        while self.keep_running:
            try:
                logging.info("Starting worker thread...")
                # print(f"Running with configuration file: \n{self.config}")

                heartbeat_results = heartbeat_check(self.config['services'])

                # Start logging to statsd if it is enabled in config file
                if 'statsd' in self.config:
                    path_prefix = self.config['statsd']['path']
                    log_to_statsd(
                        self.statsd_client,
                        path_prefix,
                        heartbeat_results)

                time.sleep(5)

            except Exception as e:
                logging.exception(f"An error occurred: {e}")

    def stop(self):
        """
        Stops the worker in case of interrupt or exceptions.
        """
        self.keep_running = False
