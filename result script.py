import requests

url = 'https://www.virustotal.com/vtapi/v2/file/report'

params = {'apikey': '<apikey>', 'resource': '<resource>'}

response = requests.get(url, params=params)

print(response.json())
