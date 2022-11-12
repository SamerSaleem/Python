import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York", "Country":"USA"}'

# parse x:
y = json.loads(x)
#y = json.load(x)

# the result is a Python dictionary:
print(y["Country"])

