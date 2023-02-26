
import requests

url = 'https://webhook.site/4355d0e6-5e16-421b-928d-040d55e2be4b'   # here we have API request to fetch data
response = requests.get(url)

jsondata = response.json()      # To get response data as JSON

# Task 1: this function separate lists on tag value
apilist_dict = {}
for i in jsondata:
    tag = i['tag']
    if tag not in apilist_dict:
        apilist_dict[tag] = []
    apilist_dict[tag].append(i)

print('.......................Here we get the ouput of separate lists on tag Value......................')
for tag, entries in apilist_dict.items():
    print(tag, ':', entries)

# Task 2: this function sort each sub-list entries by id value
for tag, entries in apilist_dict.items():
    entries.sort(key=lambda x: x['id'])

print('.......................Here we get the ouput of sort of each sub-list by id value......................')
for tag, entries in apilist_dict.items():
    print(tag, ':', entries)


# Task 3: endpoint to POST
url = 'https://webhook.site/4355d0e6-5e16-421b-928d-040d55e2be4b'
for tag in apilist_dict:
    entries = apilist_dict[tag]
    payload_data = {'entries': entries}
    response = requests.post(url, json=payload_data)
    print(response.status_code)