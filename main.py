import json
from template_engine import TemplateEngine
# from datastore.sqlite import SqliteStore

# file_name = "C:\\Users\\b\\Desktop\\spc-migrate\\mathew\\templates\\pubs.html"
# template_file = open(file_name, 'r')
# template = template_file.read()

# with SqliteStore('test.data') as data_store:
#     data_store.bootstrap()
#     data = {k: v for k, v in data_store.get_data()}

#     def get_data(m):
#         key = m.group(1)
#         return data[key]

#     TE = TemplateEngine(
#         templates_dir="C:\\Users\\b\\Desktop\\spc-migrate\\mathew\\templates")
#     result = TE.parse(template, get_data)

#     with open('build.html', 'w') as outfile:
#         outfile.write(result)

# template_file.close()

specimen = "hello world, i am birnadin erick,\n here are some { include a.html }"
data = {
    "a.html": (
        "i have a crush on {eval crush.name}, i love her {eval crush.fav}",
        [
            {"name": "Manuka K", "fav": "tt"},
            {"name": "Kaviya S", "fav": "nose"},
        ]
    ),
    "b.html": (
        "i have a crush on {eval crush.name}, i hate her {eval crush.hate}",
        [
            {"name": "Manuka K", "hate": "jealousy"},
            {"name": "Kaviya S", "hate": "ignorance"},
        ]
    ),
}

for k in data.keys():
    agg_res = parse_template(data[k][0], data[k][1])

    for i, agg_re in enumerate(agg_res):
        fname, ext = tuple(k.split("."))
        filename = fname + str(i) + '.' + ext
        with open(filename, 'w') as file:
            file.write(eval_include(specimen, agg_re))
