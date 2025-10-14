import json
pessoa ={"nome":"Carlos","idade":28,"estudante":False}
json_strings = json.dumps(pessoa)
print(json_strings)