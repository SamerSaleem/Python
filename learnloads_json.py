import json

with open ("json_sample.json") as samer:
    json_data = samer.read()

json_dict= json.loads(json_data)
print ("the data type is: ", (type(json_dict)))
print(json_dict)

#lets modify the data and print again
json_dict ['interface'] ['description'] = 'backuplink'
print(json_dict)