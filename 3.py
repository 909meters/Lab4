'''
1. dict
2. list
3. tuple
4. string
5. int
6. float
7. True
8. False
9. None
'''

import json

print(json.dumps({"first": "a", "second": "b", "third": "c"})) #1
print(json.dumps(["a", "b", "c"]))  #2
print(json.dumps(("a", "b", "c")))  #3
print(json.dumps("abc"))  #4
print(json.dumps(123))  #5 
print(json.dumps(123.45))   #6
print(json.dumps(True))   #7
print(json.dumps(False))   #8
print(json.dumps(None))    #9

