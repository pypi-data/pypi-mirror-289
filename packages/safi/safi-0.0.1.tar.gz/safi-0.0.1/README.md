safi - Pure

Safi is a versatile and high performance Ai Platform. This is a Python library for Safi APIs.

Installation

You can install this package using pip:

```sh
pip install safi


##Usage

from safi import Safi

# Get your api key 'your_api_key' from your account dashbaord on safi.insolify.com

api_key = 'your_api_key'

# Basic Usage for 
safi = Safi(api_key,'chat')
response = safi.chat('Hi Safi').go()
print(response....)

#Deleting a record operation
response = safibase.lake('test_lake').record('test_record').delete('at id='2'').run()
print(response)

# Usage with voice input
safi = safi(api_key, lang='pidgin')
response = safibase.chat(record.mp3).go()
print(response.......)
