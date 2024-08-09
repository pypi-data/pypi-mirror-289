# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['globalnoc_monitoring_service_status']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'globalnoc-monitoring-service-status',
    'version': '0.1.0',
    'description': '',
    'long_description': "# GlobalNOC Status Monitoring Library\n\nThis Python library is used to write status files for GRNOC software.\n\n---\n\n## Requirements\n\nPlease make sure you have the following dependencies already installed on your host:\n\n- `python3`\n- `python3-setuptools`\n\n## Installation\n\nRun the following command to install the library:\n\n```console\nfoo@bar:~$ sudo yum install python3-globalnoc-monitoring-service-status\n```\n\n## Import \n\nImport the `write_service_status` function using the following line of code:\n\n```python\nfrom globalnoc_monitoring_service_status import write_service_status\n```\n\n## Function Parameters\nThe `write_service_status` function has the following parameters:\n\n| Parameter | Required? |  Default Value | Description |\n| ------ | ------ | ------ | ------ |\n| `error` | Yes | - | Error Number |\n| `error_text` | Yes | - | Error Description |\n| `path` | No | - | Target folder |\n| `service` | No | - | Service Name |\n| `filename` | No | `status.txt` | Status File Name|\n| `timestamp` | No | Current Time | Unix Timestamp|\n\n**Note**: You must either provide a path to the status file folder or a service name.\n\nIf for some reason `path` and `service` are both passed as arguments, the function will create the status file at the provided `path`.\n\n## Usage\nHere are some code snippets using this module:\n\n```python\nfrom globalnoc_monitoring_service_status import write_service_status\n\n# Create status.txt at /var/lib/grnoc/fortigate_collector/\nwrite_service_status(error=0,\n                     error_text='Data queued to RabbitMQ Successfully.', \n                     service='fortigate_collector')\n\n# Create status_log at /var/lib/my_service/\nwrite_service_status(error=1,\n                     error_text='Error making GET request.', \n                     path='/var/lib/my_service/', \n                     filename='status_log')\n\n# Create status.txt at /var/lib/my_service/ with custom timestamp\nwrite_service_status(error=1,\n                     error_text='Error making GET request.', \n                     path='/var/lib/my_service/',\n                     timestamp='1596547846')\n```\n",
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
