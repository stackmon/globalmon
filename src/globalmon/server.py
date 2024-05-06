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
    parser.add_argument('--config', required=True, help='Path to the config file')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
    else:
        logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

    config_filepath = args.config

    logging.info("Loading configuration file.")
    # Check if the file extension is .yaml or .yml
    if not config_filepath.lower().endswith(('.yaml', '.yml')):
        raise ValueError("Config file must be a YAML file (.yaml or .yml)")

    # Load the config file
    config = load_config(config_filepath)

    # Your main application logic here
    print("Reading configuration:")
    print(config)

    logging.info("Creating a new worker.")
    globalmonWorker = GlobalmonWorker(config)

    # Create a new thread
    worker_thread = threading.Thread(target=globalmonWorker.run)

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