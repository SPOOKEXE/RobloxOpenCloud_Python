# Roblox Open Cloud API
## Coded in python

Contains a module which allows you to utilise open cloud on Roblox.
Start with the following;

```py
from roblox_open_cloud import Client as OpenCloudAPI, BaseEnum, Enum

# Key is necessary
OpenCloudAPI = OpenCloudClient(api_key="YOUR_API_KEY", cookies=None, headers=None)

# set the cookie for any request, optional info
OpenCloudAPI.setCookie("cookie_name", "cookie_value", "domain" or None)

# set the headers in any request, optional info
OpenCloudAPI.setHeader("header_name", "header_value")

# universe_id = integer, topic = string, data = string
resultEnum = OpenCloudAPI.PostOnMessagingService(universe_id=0, topic=None, data=None)
if resultEnum == Enum.Success:
	print("Success")
else:
	print("Unsuccessful - Reason; ", resultEnum)

[UNAVAILABLE ITEMS - FUTURE REFERENCE]
# DATASTORE API
# OpenCloudAPI.GetAllDataInDataStore(universe_id=0)
# OpenCloudAPI.GetDataFromKeyInDataStore(universe_id=0, key="key_to_search")
# OpenCloudAPI.GetDataFromKeysInDataStore(universe_id=0, key=["key_1", "key_2"])

# OpenCloudAPI.SetDataForKeyInDataStore(universe_id=0, key="key_to_search", json_data="")
# OpenCloudAPI.SetDataFromTuplesInDataStore(universe_id=0, data_tuples=[ ("key", "json_value") ])
# OpenCloudAPI.SetDataFromDictInDataStore(universe_id=0, data_dict={"key":"json_value"})
# OpenCloudAPI.SetDataFromArraysInDataStore(universe_id=0, key_array=["key_1", "key_2"], data_array=["data_1", "data_2"]) # USE for key, data in ZIP(arrayA, arrayB)

# OpenCloudAPI.ClearDataStore(universe_id=0, backupDataLocally=True)

# PUBLISH PLACE API
# OpenCloudAPI.PublishPlace(universe_id=0, filepath="")
```

Simple to use ;-)
