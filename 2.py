import json

x = { "Name": "Harry",
    "Age": "11",
    "Job": "Wizard"
}

y = json.dumps(x)

print(y)
