
# Imports
import json#, base64, hashlib
from typing import Union

from warnings import warn

from Enums import Enum, BaseEnum
from Requests import RequestsClass

from requests import Response

# Constants
MESSAGING_SERVICE_BASE_URL = "https://apis.roblox.com/messaging-service/v1/universes/{}/topics/{}"
#DATASTORE_BASE_URL = 'https://apis.roblox.com/datastores/v1/universes/{}'

# Classes
# class UniverseDataStoreWrapper:
# 	__requestsInstance = None

# 	def list_entries(self, universe_id, datastore, scope=None, prefix="", limit=100, allScopes=False, cursor_key=None) -> Union[None, list]:
# 		entry_url = DATASTORE_BASE_URL.format(universe_id) + '/standard-datastores/datastore/entries/entry'
# 		params = {
# 			"datastoreName" : datastore,
# 			"scope" : scope,
# 			"allScopes" : allScopes,
# 			"prefix" : prefix,
# 			"limit" : limit,
# 			"cursor" : cursor_key
# 		}
# 		response = self.__requestsInstance.get(entry_url, params=params)
# 		print(response.content)
# 		return None

# 	def __init__(self, requestsInstance=None):
# 		self.__requestsInstance = requestsInstance

class Client:
	__requestsInstance = None
	
	def getRequestsInstance(self) -> RequestsClass:
		return self.__requestsInstance

	# Redirecting Functions 
	def setCookie(self, cookie_name : str, cookie_value : any, domain : str) -> None:
		self.__requestsInstance.setCookie(cookie_name, cookie_value, domain)

	def setHeader(self, header_name : str, header_value : any) -> None:
		self.__requestsInstance.setHeader(header_name, header_value)

	# Class Functions
	def checkKeyValidity(self) -> bool:
		#raise NotImplementedError("Check API Key Validity is not implemented!")
		return True, "Valid Key"

	# Primary Functions
	def PostOnMessagingService(self, universe_id=0, topic=None, data=None) -> BaseEnum:
		print(universe_id, topic, data)
		if type(universe_id) != int:
			return BaseEnum(12, "ArgumentError", "Invalid Argument", custom_error="Universe Id is invalid.")
		if type(data) != str:
			return BaseEnum(13, "ArgumentError", "Invalid Argument", custom_error="Data is invalid.")
		# get a JSON string of the data
		content = json.dumps({"message" : data})
		# endcode it
		content = content.encode()
		# post to the universe id under the topic
		try:
			response = self.__requestsInstance.post(MESSAGING_SERVICE_BASE_URL.format(universe_id, topic), content)
		except:
			return None, Enum.ProgramError
		# status code custom enum message
		response_enum = Enum.ProgramError
		if response.status_code == 200:
			response_enum = Enum.Success
		elif response.status_code == 401:
			response_enum = Enum.Unavailable
		elif response.status_code == 403:
			response_enum = Enum.Unauthorized
		elif response.status_code == 500:
			response_enum = Enum.InternalError
		if response_enum != Enum.Success:
			warn(response_enum, response.content)
		return response_enum

	# TODO
	def GetDataStoreData(self, universeId : int, datastoreName : str):
		# https://apis.roblox.com/datastores/v1/universes/{universeId}/standard-datastores/datastore/entries?datastoreName={datastoreName}&entryKey={datastoreKey}
		raise NotImplemented("Has not been implemented - GetDataStoreData")
	def GetDataStoreDataFromKey(self, universeId : int, datastoreName : str, datastoreKey : str):
		# https://apis.roblox.com/datastores/v1/universes/{universeId}/standard-datastores/datastore/entries/entry?datastoreName={datastoreName}&entryKey={datastoreKey}
		raise NotImplemented("Has not been implemented - GetDataStoreDataFromKey")

	# Init
	def __init__(self, api_key=None, cookies=None, headers=None):
		self.__requestsInstance = RequestsClass(api_key=api_key, cookies=cookies, headers=headers)
