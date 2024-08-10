# impotsgouvdata

impotsgouvdata is a Python library designed to retrieve taxpayer data 
from https://www.impots.gouv.fr (the French tax administration website).

For the moment, the library only supports the retrieval of tax documents 
for private individuals.

# Installation

impotsgouvdata can be installed using pip :

```shell
pip install impotsgouvdata
```

# Usage

```python
from impotsgouvdata import ImpotsGouvData

# Create a `ImpotsGouvData` instance with a fiscal number and a password
igd = ImpotsGouvData(fiscal_number='1234567891234', password='password')

# Log on to impots.gouv.fr
igd.login()

# Get civil data
igd.last_name # 'Dupont'
igd.first_name # 'Jean'
igd.birth_date # datetime.date(1970, 6, 30)

# Iter over tax documents
for doc in igd.iter_documents():
    print(doc) # IncomeTaxNotice, IncomeTaxReturn, etc.
```

# Dependencies

impotsgouvdata makes use of the following libraries:
- [requests](https://requests.readthedocs.io/en/latest/) (Apache-2.0 license)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) (MIT license)
- [lxml](https://lxml.de/) (BSD license)


# License

impotsgouvdata is developed under [CeCILL-C](https://cecill.info/licences/Licence_CeCILL-C_V1-en.html) license.