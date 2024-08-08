# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['batched_queue']

package_data = \
{'': ['*']}

install_requires = \
['cython>=3.0.10,<4.0.0']

setup_kwargs = {
    'name': 'batched-queue',
    'version': '0.1.2',
    'description': 'Batched Queue',
    'long_description': '# Batched Queue\n',
    'author': 'Daniel Sullivan',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
