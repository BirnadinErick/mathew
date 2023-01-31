import os
from template_engine.macros import parse_template, eval_include

# base template
base = ""
with open(os.path.realpath("templates/base.html"), "r") as base_f:
    base = base_f.read()

# index compilation
index = ""
with open(os.path.realpath("templates/index.html"), "r") as index_f:
    index = index_f.read()

index_parsed = eval_include(base, index)

with open("index_parsed.html", "w") as index_out:
    index_out.write(index_parsed)

# publications compilation
pub = ""
with open(os.path.realpath("templates/pubs_template.html"), "r") as pubs_f:
    pub = pubs_f.read()

article = ""
with open(os.path.realpath("templates/article_template.html"), "r") as arts_f:
    article = arts_f.read()

ds = {
    "article.html": (
        article, [
            {"cat": "announcement", "title": "Battle of Golds 1"},
            {"cat": "celebration", "title": "St. Patrick's Day 2021"},
            {"cat": "academia", "title": "AL 2021 colors"},
            {"cat": "sports", "title": "U17 Footbal, boys come 1st runner up"},
        ]
    )
}

parsed_arts = parse_template(ds["article.html"][0], ds["article.html"][1])

with open(os.path.realpath("templates/pubs.html"), 'w') as file:
    file.write(
        eval_include(
            base,
            eval_include(pub, "".join(parsed_arts))
        )
    )
