# amazon-paapi-python-sdk

Amazon Product Advertising API 5.0 rewrited for Python.

## Features

- Multiple platforms supports and includes **asyncio**
  - support `requests` as sync mode
  - support `httpx` as async/sync mode
  - support `tornado` as async mode
  - **very easy to extend** to another platform
- Type hints for every interface 
- Support **ALL data models** for PAAPI to help you coding.
- Object oriented interface for simple usage.
- Get information about a product through its ASIN or URL.
- Get item variations or search for products on Amazon.
- Get browse nodes information.
- Get multiple results at once without the 10 items limitation from Amazon.
- Support for all available countries.

## Installation

You can install or upgrade the module with:

    pip install amazon-paapi-python-sdk --upgrade

## Usage guide

**Basic usage**

```python

from amazon_paapi_python_sdk import PaapiClient

client = PaapiClient(ACCESS_KEY, SECRET_KEY, PARTNER_TAG)
items = client.get_items(['B01N5IB20Q', 'B01F9G43WU'])
for items in items:
    print(item.images.primary.large.url) # primary image url
    print(item.offers.listings[0].price.amount) # current price

```

