import json
import re

def json_formator(data):
    json_data = json.dumps(data, sort_keys=True)

    with open('jsondata.json', 'r') as r:
        if not r.read():
            open('jsondata.json', 'w').write(json_data)
        else:
            open('jsondata.json', 'a').write(json_data)

    with open('jsondata.json', 'r+') as f:
        searchlines = f.read()
        print(searchlines)
        if re.search('\}\{', searchlines):
            w = open('jsondata.json', 'w')
            replacedlines = re.sub('\}\{', ', ', searchlines)
            w.write(replacedlines)
            print('\n')
            print(replacedlines)

