# COMPONENTS OVERVIEW

``` bash
+---------------------------------------------------------------+
|                           server.py                           |
|---------------------------------------------------------------|
| + loadconfig()                                                |
| + main()                                                      |
|    |                                                          |
|    | creates and starts thread                                |
|    v                                                          |
|  +------------------------------+                             |
|  |       GlobalmonWorker        |                             |
|  |------------------------------|                             |
|  | - __init__(config)           |                             |
|  | - run(period)                |                             |
|  | - stop()                     |                             |
|  +------------------------------+                             |
|          |                                                    |
|          | uses                                               |
|          v                                                    |
|  +-------------------------------------------------------+    |
|  |                      utils.py                         |    |
|  |-------------------------------------------------------|    |
|  | + heartbeat_check(services)                           |    |
|  | + initialize_statsd_client(host, port)                |    |
|  | + log_to_statsd(statsd_client, path_prefix, results)  |    |
|  +-------------------------------------------------------+    |
+---------------------------------------------------------------+
```

## Diagram Key

* server.py: The entry point that includes main() and loadconfig().
* GlobalmonWorker: The main worker class with methods to run and stop the monitoring process.
* utils.py: A utility module containing helper functions.

## Explanation

*server.py* contains the main() function, which loads the configuration using loadconfig(), creates an instance of GlobalmonWorker, and starts its run() method in a new thread.

**GlobalmonWorker** is the class that performs the monitoring tasks. It uses functions from utils.py such as *heartbeat_check*, *initialize_statsd_client*, and *log_to_statsd* to perform its tasks.

*utils.py* contains helper functions that assist in the monitoring process, such as checking the health of services, initializing the StatsD client, and logging data to StatsD.
