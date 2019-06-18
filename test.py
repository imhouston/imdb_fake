import requests

my_json = {"query": "text",
           "params": {"boostingFields": {"fieldName1": "fieldWeight1", "fieldName2": "fieldWeight2"}}}

res = requests.post('http://localhost:5002/search', json=my_json)
if res.ok:
    print(res.json())
