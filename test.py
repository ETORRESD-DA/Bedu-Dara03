import json

f = open("tmp/base.json", "r")
content = f.read()
jsondecoded = json.loads(content)

for elemento in jsondecoded:
    print(elemento['login'])
    print("\n")