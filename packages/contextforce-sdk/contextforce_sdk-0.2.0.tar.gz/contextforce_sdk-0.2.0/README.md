# ContextForce Python SDK

## Packaging and Publish
```bash
# install poetry
curl -sSL https://install.python-poetry.org | python3 -

# check version
poetry --version

# create new poetry project
poetry new contextforce_sdk

# add library
poetry add requests

# export
poetry export --output requirements.txt

# package the code into .whl file
poetry build

# After executing the poetry publish command, your package will be published on the Python Package Index (PyPI), 
# which makes it available for installation through Poetry.
poetry publish

```

## Installation
You can install the package using pip:

```bash
pip install contextforce_sdk
```

## Usage
To use the package, you must first obtain an API key from NumLookupAPI. Once you have an API key, you can create a PhoneNumberValidator instance and use its validate method to validate a phone number:

```python
from contextforce_sdk import ContextForceClient

api_key = 'your_api_key_here'
client = ContextForceClient(api_key=api_key)

pdf_file_path = 'path_to_your_pdf_file.pdf'

with open(pdf_file_path, 'rb') as file:
    pdf_content = file.read()

result = client.extract_pdf(
    pdf_source=pdf_content,
    result_format='markdown',
    model='gpt-4o-mini',
    openai_api_key='your_openai_api_key'
)

print(result)
```
