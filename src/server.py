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

def load_config(config_file):
    try:
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)
        return config
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing YAML file: {e}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config-file', required=True, help='Path to the config file')
    args = parser.parse_args()

    config_filepath = args.config_file

    # Check if the file extension is .yaml or .yml
    if not config_filepath.lower().endswith(('.yaml', '.yml')):
        raise ValueError("Config file must be a YAML file (.yaml or .yml)")

    # Load the config file
    config = load_config(config_filepath)

    # Your main application logic here
    print("Reading configuration:")
    print(config)

if __name__ == "__main__":
    main()