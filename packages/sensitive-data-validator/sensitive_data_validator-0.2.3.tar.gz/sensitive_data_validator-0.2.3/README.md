# Sensitive Data Validator

A package to validate sensitive data in various file formats.

## Installation

You can install the package using pip:

```bash
pip install sensitive_data_validator


```

Example code:

```bash

from sensitive_data_validator import SensitiveAPI

# Exemplo de uso com personalização de campos
api = SensitiveAPI(fields_to_check=['BRAZIL_PERSONAL_ID', 'EMAIL'])
result = api.file_check('example.json', filetype='json')
print(result)

# Exemplo de uso sem personalização de campos (verificando todos os campos)
api = SensitiveAPI()
result = api.file_check('example.json', filetype='json')
print(result)


