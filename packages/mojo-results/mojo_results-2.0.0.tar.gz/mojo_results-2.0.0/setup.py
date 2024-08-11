# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'source/packages'}

packages = \
['mojo',
 'mojo.results',
 'mojo.results.concentrators',
 'mojo.results.model',
 'mojo.results.recorders']

package_data = \
{'': ['*']}

install_requires = \
['mojo-errors>=2.0.0,<2.1.0', 'mojo-xmodules>=2.0.0,<2.1.0']

setup_kwargs = {
    'name': 'mojo-results',
    'version': '2.0.0',
    'description': 'The Automation Mojo Results Package',
    'long_description': "=======================\nMojo Results Package\n=======================\nThis package contains code elements for working with automation results.\n\n=========================\nFeatures of this Template\n=========================\n* Machine Setup\n* Virtual Environment Setup (Poetry)\n* PyPi Publishing\n* Sphinx Documentation\n\n=================\nCode Organization\n=================\n* .vscode - Common tasks\n* development - This is where the runtime environment scripts are located\n* repository-setup - Scripts for homing your repository and to your checkout and machine setup\n* userguide - Where you put your user guide\n* source/packages - Put your root folder here 'source/packages/(root-module-folder)'\n* source/sphinx - This is the Sphinx documentation folder\n* workspaces - This is where you add VSCode workspaces templates and where workspaces show up when homed.\n\n==========\nReferences\n==========\n\n- `User Guide <userguide/userguide.rst>`\n- `Coding Standards <userguide/10-00-coding-standards.rst>`\n",
    'author': 'Myron W. Walker',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
