import json

x = '{ "Name": "Harry", "Age": "11", "Job": "Wizard"}'

y = json.loads(x)

print(y["Age"])