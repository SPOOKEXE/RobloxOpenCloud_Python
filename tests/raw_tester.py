
# Imports
from roblox_open_cloud_api import *

baseClient = Client(api_key="NE+w3rIcnE2e/WyJtKawQwOfHq3My6Uip59yfoLPeMYSXc7T")

url = 'https://apis.roblox.com/datastores/v1/universes/{}'.format(3424752311)

print(baseClient.getRequestsInstance())
response = baseClient.getRequestsInstance().get(url)

print(response.content)
