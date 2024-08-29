# globalmon

Globalmon is a static global monitoring application written in Python. Globalmon queries the list of urls provided for each service and passes the results to Graphite TSDB via Statsd daemon.

Using Globalmon, you can continuously monitor reachability and return times for hosted services.

## Getting started

The globalmon requires the following to work.
- Python3
- Docker or similar tool (for containerized installation)
- StatsD
- Graphite
- setuptools (for local installation)

Globalmon is also dependent on configuration file in yaml format. A sample configuration file, *config.yaml*, is included in base directory.

## Useful Links

* [Install Docker Engine on Linux](https://docs.docker.com/desktop/install/linux-install/)
* [Install and run StatsD/Graphite](https://graphite.readthedocs.io/en/latest/install.html)

## Quickstart

### Configuration

Globalmon configuration is a simple yaml file with services and statsd information defined in there.

```yaml
services:
  myservice1:
    urls:
      - "https://myservice1.example.com"
  myservice2:
    urls:
      - "https://myservice2.example.com"
statsd:
  host: "{STATSD_HOST}"
  port: 8125
  path: "globalmon.{env}.{zone}"
```

***NOTE:*** Use fully qualified domain names in URLS **including protocol (http/https)**.

You can monitor any service and any URLs. Replace the ```STATSD_HOST``` with address of your statsd daemon. 
Path can be anything you decide. However, some characters such as ```/``` might create unusual behaviour in StatsD. Using the format shown above, your metrics should be found in Graphite under the path ```Metrics/stats/timers/globalmon/{env}/{zone}/``` and ```Metrics/stats/counter/globalmon/{env}/{zone}/```. 

### Local Installation

To build and install the globalmon package use the following command:

```
python3 setup.py install
```

Once the install is completed, globalmon can be executed as:

```bash
usage: globalmon [-h] --config CONFIG [--debug] [--period PERIOD]

options:
  -h, --help       show this help message and exit
  --config CONFIG  Path to the config file
  --debug          Enable debug mode
  --period PERIOD  Time period between consecutive queries (in seconds)
```

For example...
```
globalmon --config /Path/to/your/config.yaml
```

### Containerized Installation

To build the globalmon image use the following command:

```
docker build -t globalmon:latest .
```

The image globalmon will be built with the tag latest. In practive, version tags should be used. The image can then be executed with the following command:

```
docker run globalmon
```

**NOTE:** In this case the globalmon will execute the config file at default location i.e. */usr/app/globalmon/config.yaml*. This file is taken at build time from config.yaml.

To pass the config file to the globalmon at runtime, we use the following command:
```
docker run -v /path/to/config.yaml:/usr/app/globalmon/config.yaml globalmon
```
**OR**
```
docker run -v /path/to/config.yaml:/some/other/path/config.yaml globalmon --config /some/other/path/config.yaml
```

**NOTE:** Latest Globalmon images can be found at https://quay.io/repository/stackmon/globalmon?tab=tags