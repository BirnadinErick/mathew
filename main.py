import json
from template_engine import TemplateEngine
from datastore.sqlite import SqliteStore

template_file = open('test.html', 'r')
template = template_file.read()

data_file = open('data.json', 'r')
data = json.loads(data_file.read())

with SqliteStore('test.data') as data_store:
    data_store.bootstrap()
    data = {k: v for k, v in data_store.get_data()}

    def get_data(m):
        key = m.group(1)
        return data[key]

    TE = TemplateEngine()
    result = TE.parse(template, get_data)

    with open('build.html', 'w') as outfile:
        outfile.write(result)

template_file.close()
data_file.close()
