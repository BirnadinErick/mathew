from template_engine.macros import parse_template, eval_include

main_template = "this is a main template, this includes { include article.html }"
article_template = "today, we are going to { map pubs.type } that { map pubs.title }"

datastore = {
    "article.html": (
        article_template, [
            {"type": "announce", "title": "SPC goes full on full digital"},
            {"type": "introduce", "title": "SPC goes full on full analogue"},
            {"type": "celebrate",
                "title": "SPC becomes first in nation in chess championship"},
            {"type": "announce",
                "title": "Our student Mathew won the All-Island Tennis Trophy"},
        ]
    )
}

results = {}

for key in datastore.keys():
    substitutions = parse_template(datastore[key][0], datastore[key][1])

    for idx, substitution in enumerate(substitutions):
        results[str(idx)] = eval_include(main_template, substitution)
        print(results[str(idx)])  # debug purpose
