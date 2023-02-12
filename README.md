# pyutils - A Collection of General-Purpose Utilities

pyutils is a Python library that contains a collection of small, reusable functions to help perform various general-purpose tasks. The library was designed to provide an efficient and convenient solution for developers who need to perform simple, common tasks without having to write long, complex code.

## Contents

- network.py
  - is_connected(): Returns a boolean indicating if the internet is connected.
  - get_local_ip(): Returns the local IP address.
  - get_public_ip(): Returns the public IP address.
- validators.py
  - is_valid_email(email: str): Returns a boolean indicating if the email is valid.
  - is_valid_phone_number(phone_number: str): Returns a boolean indicating if the phone number is valid.
  - is_valid_url(url: str): Returns a boolean indicating if the URL is valid.

## Usage

### network.py

```python
import pyutils.network as network

if network.is_connected():
    print("The internet is connected")
else:
    print("The internet is not connected")

local_ip = network.get_local_ip()
print(f"Local IP address: {local_ip}")

public_ip = network.get_public_ip()
print(f"Public IP address: {public_ip}")
```

### validators.py

```python
import pyutils.validators as validators

email = "example@example.com"
if validators.is_valid_email(email):
    print(f"{email} is a valid email.")
else:
    print(f"{email} is not a valid email.")

phone_number = "+1-555-555-5555"
if validators.is_valid_phone_number(phone_number):
    print(f"{phone_number} is a valid phone number.")
else:
    print(f"{phone_number} is not a valid phone number.")

url = "https://www.example.com"
if validators.is_valid_url(url):
    print(f"{url} is a valid URL.")
else:
    print(f"{url} is not a valid URL.")
```
