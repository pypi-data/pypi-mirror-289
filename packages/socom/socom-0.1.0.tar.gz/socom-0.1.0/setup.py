# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['socom']

package_data = \
{'': ['*']}

install_requires = \
['pybind11>=2.8.0']

setup_kwargs = {
    'name': 'socom',
    'version': '0.1.0',
    'description': 'Data analysis tool for studying social communication',
    'long_description': '# SOcial COMmunication Library\n\n**Socom** is a python package for the analysis of social communication using network-based approaches created and maintained by the Uppsala University Information Laboratory ([InfoLab](https://uuinfolab.github.io).\n\n\nWhile the ideas behind _socom_ have been developed during years, the active development of the library has not started until recently (March 2024). Therefore, be aware that this is a pre-alpha version of the library with limited functionality.\n\n\n## Contact\n\nFor any inquiries regarding the library you can contact <davide.vega@it.uu.se>',
    'author': 'Davide Vega',
    'author_email': 'davide.vega@it.uu.se',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
