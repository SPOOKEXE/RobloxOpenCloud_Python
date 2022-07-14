
ROBLOX_OPEN_CLOUD_API_KEY = ""

MESSAGING_SERVICE_BASE_URL = "https://apis.roblox.com/messaging-service/v1/universes/{}/topics/{}"
USER_AGENT_DATA = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Mobile Safari/537.36"

import requests
import json

requestsSession = requests.Session()

# force json format
requestsSession.headers["Content-Type"] = "application/json"
# set user agent data manually
requestsSession.headers['User-Agent'] = USER_AGENT_DATA
# set the api key for open cloud
requestsSession.headers['x-api-key'] = ROBLOX_OPEN_CLOUD_API_KEY

# Get all data under a datastoreName
# def GetDataStoreDataList(universeId : int, datastoreName : str):
# 	raise NotImplemented("Has not been implemented - GetDataStoreDataList")

# # Get a specific key's data, otherwise returning None if its not available
# def GetDataStoreKeyData(universeId : int, datastoreName : str, datastoreKey : str):
# 	# https://apis.roblox.com/datastores/v1/universes/{universeId}/standard-datastores/datastore/entries/entry?datastoreName={datastoreName}&entryKey={datastoreKey}
# 	raise NotImplemented("Has not been implemented - GetDataStoreKeyData")

# Post a message to the messaging service in all games
def PostMessageServiceMessage(universeId : int, topic : str, content : str):
	print(universeId, topic, content)
	if type(content) != str:
		print("Invalid data entering post MessagingService : pass a JSON string or string through.")
		return False
	# get a JSON string of the data
	content = json.dumps({"message" : content})
	# endcode it
	content = content.encode()
	# post to the universe id under the topic
	response = requestsSession.post(MESSAGING_SERVICE_BASE_URL.format(universeId, topic), content)
	response_msg = "Unknown Error"
	# status code custom message
	if response.status_code == 200:
		response_msg = "Success!"
	elif response.status_code == 401:
		response_msg = "Unauthorized! Check the API key validity."
	elif response.status_code == 403:
		response_msg = "Not allowed on specified universe! Have you set publish permissions under the API Key settings?"
	elif response.status_code == 500:
		response_msg = "Unknown Error from Roblox server!"
	print(response, response_msg)
	return response, response_msg

# Tester
if __name__ == "__main__":
	print("[TESTER] Send message to roblox servers.")
	# https://www.roblox.com/games/9115513079/Analytic-Test
	PostMessageServiceMessage( 3424752311, "TestTopic", "test message!" )
	print("[TESTER] Published to roblox servers. Check for the message!")
