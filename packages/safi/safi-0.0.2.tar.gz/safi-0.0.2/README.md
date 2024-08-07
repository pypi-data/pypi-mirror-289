safi - Pure

Safi is a versatile and high performance Ai Platform. This is a Python library for Safi APIs.

Installation

You can install this package using pip:

```sh
pip install safi


##Usage

from safi import Safi

# Get your api key from your account dashbaord on safi.insolify.com

# Basic Usage for 
safi = Safi(api_key)
response = safi.chat('Hi Safi').go()
print(response....)


# Usage with voice input
safi = Safi(api_key, lang='pidgin')
response = safi.chat(record.mp3).go()
print(response.......)

#Transcription/Dictation
safi = safi(api_key, lang='pidgin')
response = safi.listen(input_audio) 
print(response[0]....) #chunks..
#This can be real time audio stream from speaker or microphone or direct audio.

Other use cases can be explored from your dashboard.