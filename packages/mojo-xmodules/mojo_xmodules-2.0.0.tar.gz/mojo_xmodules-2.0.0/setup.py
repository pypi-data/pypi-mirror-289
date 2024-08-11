# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'source/packages'}

packages = \
['mojo',
 'mojo.xmods',
 'mojo.xmods.eventing',
 'mojo.xmods.extension',
 'mojo.xmods.injection',
 'mojo.xmods.injection.coupling',
 'mojo.xmods.injection.decorators',
 'mojo.xmods.modeling',
 'mojo.xmods.wrappers',
 'mojo.xmods.xdata',
 'mojo.xmods.xdata.generators',
 'mojo.xmods.xlogging',
 'mojo.xmods.xmultiprocessing',
 'mojo.xmods.xthreading']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.5,<9.0.0',
 'debugpy>=1.6.6,<2.0.0',
 'mojo-collections>=2.0.1,<2.1.0',
 'mojo-errors>=2.0.0,<2.1.0',
 'mojo-interfaces>=2.0.0,<2.1.0',
 'mojo-waiting>=2.0.0,<2.1.0',
 'paramiko>=3.1.0,<4.0.0']

setup_kwargs = {
    'name': 'mojo-xmodules',
    'version': '2.0.0',
    'description': 'Automation Mojo X-Modules',
    'long_description': '\n=========================================\nAutomation Mojo X-Modules (mojo-xmodules)\n=========================================\n\nThis package contains helper modules that extend the function of standard python modules.\n\n==========\nReferences\n==========\n\n- `User Guide <userguide/userguide.rst>`_\n- `Coding Standards <userguide/10-00-coding-standards.rst>`_\n\n\n',
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
