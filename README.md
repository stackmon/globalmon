# global-mon
Global URL monitoring

## Introduction

## Requirements

The globalmon requires the following to work.
- Python3
- Docker or similar tool

Globalmon is also dependent on configuration file in yaml format. A sample configuration file, *sample_config.yaml*, is included in *quickstart* directory. 

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



