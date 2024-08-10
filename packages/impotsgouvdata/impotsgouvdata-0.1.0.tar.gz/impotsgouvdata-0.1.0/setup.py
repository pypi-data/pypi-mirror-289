# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['impotsgouvdata']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.12.3,<5.0.0',
 'lxml>=5.2.2,<6.0.0',
 'requests>=2.32.3,<3.0.0']

setup_kwargs = {
    'name': 'impotsgouvdata',
    'version': '0.1.0',
    'description': 'Retrieve taxpayer data from impots.gouv.fr.',
    'long_description': "# impotsgouvdata\n\nimpotsgouvdata is a Python library designed to retrieve taxpayer data \nfrom https://www.impots.gouv.fr (the French tax administration website).\n\nFor the moment, the library only supports the retrieval of tax documents \nfor private individuals.\n\n# Installation\n\nimpotsgouvdata can be installed using pip :\n\n```shell\npip install impotsgouvdata\n```\n\n# Usage\n\n```python\nfrom impotsgouvdata import ImpotsGouvData\n\n# Create a `ImpotsGouvData` instance with a fiscal number and a password\nigd = ImpotsGouvData(fiscal_number='1234567891234', password='password')\n\n# Log on to impots.gouv.fr\nigd.login()\n\n# Get civil data\nigd.last_name # 'Dupont'\nigd.first_name # 'Jean'\nigd.birth_date # datetime.date(1970, 6, 30)\n\n# Iter over tax documents\nfor doc in igd.iter_documents():\n    print(doc) # IncomeTaxNotice, IncomeTaxReturn, etc.\n```\n\n# Dependencies\n\nimpotsgouvdata makes use of the following libraries:\n- [requests](https://requests.readthedocs.io/en/latest/) (Apache-2.0 license)\n- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) (MIT license)\n- [lxml](https://lxml.de/) (BSD license)\n\n\n# License\n\nimpotsgouvdata is developed under [CeCILL-C](https://cecill.info/licences/Licence_CeCILL-C_V1-en.html) license.",
    'author': 'Pierre Gobin',
    'author_email': 'p.dev@gobin.cc',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
