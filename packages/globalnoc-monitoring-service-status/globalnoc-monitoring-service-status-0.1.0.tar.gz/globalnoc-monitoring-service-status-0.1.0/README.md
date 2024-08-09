# GlobalNOC Status Monitoring Library

This Python library is used to write status files for GRNOC software.

---

## Requirements

Please make sure you have the following dependencies already installed on your host:

- `python3`
- `python3-setuptools`

## Installation

Run the following command to install the library:

```console
foo@bar:~$ sudo yum install python3-globalnoc-monitoring-service-status
```

## Import 

Import the `write_service_status` function using the following line of code:

```python
from globalnoc_monitoring_service_status import write_service_status
```

## Function Parameters
The `write_service_status` function has the following parameters:

| Parameter | Required? |  Default Value | Description |
| ------ | ------ | ------ | ------ |
| `error` | Yes | - | Error Number |
| `error_text` | Yes | - | Error Description |
| `path` | No | - | Target folder |
| `service` | No | - | Service Name |
| `filename` | No | `status.txt` | Status File Name|
| `timestamp` | No | Current Time | Unix Timestamp|

**Note**: You must either provide a path to the status file folder or a service name.

If for some reason `path` and `service` are both passed as arguments, the function will create the status file at the provided `path`.

## Usage
Here are some code snippets using this module:

```python
from globalnoc_monitoring_service_status import write_service_status

# Create status.txt at /var/lib/grnoc/fortigate_collector/
write_service_status(error=0,
                     error_text='Data queued to RabbitMQ Successfully.', 
                     service='fortigate_collector')

# Create status_log at /var/lib/my_service/
write_service_status(error=1,
                     error_text='Error making GET request.', 
                     path='/var/lib/my_service/', 
                     filename='status_log')

# Create status.txt at /var/lib/my_service/ with custom timestamp
write_service_status(error=1,
                     error_text='Error making GET request.', 
                     path='/var/lib/my_service/',
                     timestamp='1596547846')
```
