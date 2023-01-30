import json
from template_engine import TemplateEngine
from datastore.sqlite import SqliteStore

file_name = "C:\\Users\\b\\Desktop\\spc-migrate\\mathew\\templates\\pubs.html"
template_file = open(file_name, 'r')
template = template_file.read()

with SqliteStore('test.data') as data_store:
    data_store.bootstrap()
    data = {k: v for k, v in data_store.get_data()}

    def get_data(m):
        key = m.group(1)
        return data[key]

    TE = TemplateEngine(
        templates_dir="C:\\Users\\b\\Desktop\\spc-migrate\\mathew\\templates")
    result = TE.parse(template, get_data)

    with open('build.html', 'w') as outfile:
        outfile.write(result)

template_file.close()
