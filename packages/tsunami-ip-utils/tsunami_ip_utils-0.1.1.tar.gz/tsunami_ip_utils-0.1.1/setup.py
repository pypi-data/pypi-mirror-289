# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['tsunami_ip_utils', 'tsunami_ip_utils.viz']

package_data = \
{'': ['*'],
 'tsunami_ip_utils': ['input_files/*'],
 'tsunami_ip_utils.viz': ['assets/*', 'css/*']}

install_requires = \
['IPython',
 'dash',
 'flask',
 'h5py',
 'kaleido',
 'matplotlib',
 'openpyxl',
 'pandas',
 'plotly>=5.22.0,<5.23.0',
 'pyprojroot',
 'pytest',
 'pytest-mpl',
 'pyyaml',
 'scipy',
 'selenium',
 'tqdm',
 'uncertainties',
 'webdriver-manager']

setup_kwargs = {
    'name': 'tsunami-ip-utils',
    'version': '0.1.1',
    'description': 'A tool for visualizing similarity data from the SCALE code: TSUNAMI-IP',
    'long_description': "# Introduction\nThis is a python package created to provide enhanced visualization capabilities for criticality safety similarity indices calculated by\n[TSUNAMI-IP](https://scale-manual.ornl.gov/tsunami-ip.html#tsunami-ip): a code in the Standardized Computer Analysis for Licensing Evaluation ([SCALE](https://scale-manual.ornl.gov/)) suite. These methods are still under development and are *not* intended for\nproduction use, but can be nice as an exploratory tool.\n\n# Installation and Setup\nThis package is [published on PyPI](https://pypi.org/project/tsunami-ip-utils/), and so can be installed (along with all of the necessary dependencies) via `pip`\n```\npip install tsunami_ip_utils\n```\n\n# Documentation and Examples\nIf you're interested in running some examples, just clone this repository via the instructions [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository) and navigate to the `examples` directory.\nMore detailed instructions (in a human readable form) can be found in [the documentation](https://mlouis9.github.io/tsunami_ip_utils/),\nalong with a description of the theory behind the visualization tools, and a fully documented API.\n",
    'author': 'Matthew Louis',
    'author_email': 'matthewlouis31@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
