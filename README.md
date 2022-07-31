# yunite.py

An easy to use Yunite API wrapper written in Python.

## Key Features
- Asynchronus functions 
- Speed optimization 
- Easy to use 

## Installation

To install the library you can use the following command, please note that you have to have `git` installed.

```
# Mac / Linux
python3 -m pip install -U git+https://github.com/nmsturcke/yunite.py

# Windows
py -m pip install -U git+https://github.com/nmsturcke/yunite.py
```

## Quick Example

```
from yunite import YuniteClient

client = YuniteClient(yunite_api_key="YOUR-API-KEY", fortnite_api_key="YOUR-API-KEY")

print(client.id)
print(client.name)
print(", ".join(guild.name for guild in client.guilds))
```

You can find more examples in the [examples](/examples/) folder

*Please note this is an unofficial wrapper*