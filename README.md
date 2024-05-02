# global-mon
Global URL monitoring

## Introduction

## Requirements

The globalmon requires the following to work.
- Python3
- Docker or similar tool

Globalmon is also dependent on configuration file in yaml format. A sample configuration file, *config.yaml*, is included in base directory. 

## Quickstart

### Local Installation

To build and install the globalmon package use the following command:

```
python3 setup.py install
```

Once the install is completed, globalmon can be executed as:

```
globalmon --config-file *path/to/your/config.yaml*
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
docker run -v /path/to/config.yaml:/some/other/path/config.yaml globalmon --config-file /some/other/path/config.yaml
```