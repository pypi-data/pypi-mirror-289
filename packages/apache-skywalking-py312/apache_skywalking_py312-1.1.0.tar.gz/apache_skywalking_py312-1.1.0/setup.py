# -*- coding: utf-8 -*-
from setuptools import setup
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

packages = \
['skywalking',
 'skywalking.agent',
 'skywalking.agent.protocol',
 'skywalking.bootstrap',
 'skywalking.bootstrap.cli',
 'skywalking.bootstrap.cli.utility',
 'skywalking.bootstrap.hooks',
 'skywalking.bootstrap.loader',
 'skywalking.client',
 'skywalking.command',
 'skywalking.command.executors',
 'skywalking.log',
 'skywalking.meter',
 'skywalking.meter.pvm',
 'skywalking.plugins',
 'skywalking.profile',
 'skywalking.protocol',
 'skywalking.protocol.browser',
 'skywalking.protocol.common',
 'skywalking.protocol.ebpf',
 'skywalking.protocol.event',
 'skywalking.protocol.language_agent',
 'skywalking.protocol.logging',
 'skywalking.protocol.management',
 'skywalking.protocol.profile',
 'skywalking.protocol.service_mesh_probe',
 'skywalking.trace',
 'skywalking.utils',
 'sw_python',
 'sw_python.src']

package_data = \
{'': ['*']}

install_requires = \
['grpcio', 'grpcio-tools', 'packaging', 'psutil<=5.9.5', 'wrapt']

extras_require = \
{'all': ['requests>=2.26.0',
         'kafka-python',
         'uvloop>=0.17.0,<0.18.0',
         'aiokafka>=0.8.0,<0.9.0',
         'aiohttp>=3.7.4,<4.0.0'],
 'async': ['uvloop>=0.17.0,<0.18.0',
           'aiokafka>=0.8.0,<0.9.0',
           'aiohttp>=3.7.4,<4.0.0'],
 'asynchttp': ['uvloop>=0.17.0,<0.18.0', 'aiohttp>=3.7.4,<4.0.0'],
 'asynckafka': ['uvloop>=0.17.0,<0.18.0', 'aiokafka>=0.8.0,<0.9.0'],
 'http': ['requests>=2.26.0'],
 'kafka': ['kafka-python'],
 'sync': ['requests>=2.26.0', 'kafka-python']}

entry_points = \
{'console_scripts': ['sw-python = skywalking.bootstrap.cli.sw_python:start']}


setup_kwargs = {
    'name': 'apache-skywalking-py312',
    'version': '1.1.0',
    'description': 'The Python Agent for Apache SkyWalking, which provides the native tracing/metrics/logging/profiling abilities for Python projects.',
    'author': 'Apache Software Foundation',
    'author_email': 'dev@skywalking.apache.org',
    'maintainer': 'Apache SkyWalking Community',
    'maintainer_email': 'dev@skywalking.apache.org',
    'url': 'https://skywalking.apache.org/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.12,<4.0',
}


setup(**setup_kwargs)
