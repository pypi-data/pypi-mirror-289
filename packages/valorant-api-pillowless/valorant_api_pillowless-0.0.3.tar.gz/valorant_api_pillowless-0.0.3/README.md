# valorant-api-pillowless
Sync/Async Python wrapper for valorant-api.com without the pillow dependency. Pillow has been removed in order to reduce the size of the requirements for this project. The primary purpose of this package is to be used in the [Valorant-Python-Wrapper](https://github.com/Whitelisted1/Valorant-Python-Wrapper) project. Please check out the original project [here](https://github.com/MinshuG/valorant-api).

[![pypi](https://img.shields.io/pypi/v/valorant-api-pillowless.svg)](https://pypi.python.org/pypi/valorant-api-pillowless/)
[![Downloads](https://static.pepy.tech/personalized-badge/valorant-api-pillowless?period=total&units=international_system&left_color=green&right_color=blue&left_text=Downloads)](https://pepy.tech/project/valorant-api-pillowless)

# Installation
<!-- `pip install git+https://github.com/MinshuG/valorant-api-pillowless` \
or \ -->
`pip install valorant-api-pillowless`

# Usages
```py
# this code is just for reference

from valorant_api import SyncValorantApi, AsyncValorantApi

#sync
api = SyncValorantApi(language="ru-RU")
agents = api.get_agents()

#Async
api = AsyncValorantApi(language="ru-Ru")
agents = await api.get_agents()

# searching
agent = agents.find_where(displayname="Raze", developerName="Gumshoe")
agent = agents.find_first(displayname="Raze")
```

# Requirements

* python-dateutil
* aiohttp
* requests
