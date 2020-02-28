import json

x = {
    "name": "Harry",
    "surename": "Potter",
    "age": "16",
    "studing in Hogwarts": True,
    "has bad marks": False,
    "best friends": ("Hermione", "Ron"),
    "criminal cases": None,
    "adventures": [
        {"first": "The Philosopher's (Sorcerer's) Stone", "rating": "8.2"},
        {"second": "the Chamber of Secrets", "rating": "8.4" }
    ]


}
n = int(input(5))
print(json.dumps(x, indent = n))