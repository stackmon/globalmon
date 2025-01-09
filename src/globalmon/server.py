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
# limitations under the License.


import argparse
import yaml
import threading
import logging
from logging.handlers import RotatingFileHandler
from globalmon.globalmon_worker import GlobalmonWorker


def load_config(config_file):
    """
    Loads YAML configuration file from path `config_file` and
    returns python object.
    """
    try:
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)
        return config
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing YAML file: {e}")


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--config',
        required=True,
        help='Path to the config file')
    parser.add_argument(
        '--debug',
        action='store_true',
        help='Enable debug mode')
    parser.add_argument(
        '--period',
        type=int,
        required=False,
        default=10,
        help='Time period between consecutive queries (in seconds)')
    args = parser.parse_args()

    period = args.period

    # Define the log file location
    log_file = "/var/log/globalmon/globalmon.log"

    # Create a custom logger
    logger = logging.getLogger("globalmon_logger")

    if args.debug:
        # Set the level of the logger to DEBUG
        logger.setLevel(logging.DEBUG)
    else:
        # Set the level of the logger to WARNING (INFO messages will be
        # excluded)
        logger.setLevel(logging.WARNING)

    # Create a rotating file handler
    # Max file size: 5 MB, keep 3 backup files
    handler = RotatingFileHandler(
        log_file, maxBytes=5 * 1024 * 1024,
        backupCount=3)

    # Set the format for the logs
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    config_filepath = args.config

    logger.info("Loading configuration file.")
    # Check if the file extension is .yaml or .yml
    if not config_filepath.lower().endswith(('.yaml', '.yml')):
        raise ValueError("Config file must be a YAML file (.yaml or .yml)")

    # Load the config file
    config = load_config(config_filepath)

    # Your main application logic here
    print("Reading configuration:")
    print(config)

    logger.info("Creating a new worker.")
    globalmonWorker = GlobalmonWorker(config)

    # Create a new thread
    worker_thread = threading.Thread(target=globalmonWorker.run(period))

    try:
        # Start the thread
        worker_thread.start()

        # Wait for the thread to finish
        worker_thread.join()
    except KeyboardInterrupt:
        print("Keyboard interrupt received. Stopping the program...")
        globalmonWorker.stop()  # Signal the worker to stop
        worker_thread.join()  # Wait for the worker thread to finish

    print("Exiting gracefully.")


if __name__ == "__main__":
    main()
