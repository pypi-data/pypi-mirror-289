# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'source/packages'}

packages = \
['mojo', 'mojo.runtime']

package_data = \
{'': ['*']}

install_requires = \
['coverage>=7.0.4,<8.0.0',
 'mojo-collections>=2.0.1,<2.1.0',
 'mojo-config>=2.0.2,<2.1.0',
 'mojo-errors>=2.0.0,<2.1.0',
 'mojo-extension>=2.0.4,<2.1.0',
 'mojo-xmodules>=2.0.0,<2.1.0']

setup_kwargs = {
    'name': 'mojo-runtime',
    'version': '2.0.0',
    'description': 'Automation Mojo Runtime Module (mojo-runtime)',
    'long_description': '# Automation Mojo Runtime\nThe Automation Mojo - Runtime package is used to create various types of runtime environments\nsuch as Test Run, Console Command, Interactive Console and Service.  The package helps provide\nthe functionality and expected behaviors for path management and logging for each of these\ntypes of application environments.\n',
    'author': 'Myron Walker',
    'author_email': 'myron.walker@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'http://automationmojo.com',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
