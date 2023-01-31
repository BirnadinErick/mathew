import re

pattern = r'{\s?\w+\s(\w+.\w+)\s?}'


def eval_map(string, data, pattern):
    parsed = re.sub(
        pattern, lambda m: data[m.group(1).split(".")[1]], string
    )
    return parsed


def parse_template(template, data):
    global pattern
    result = []
    for datum in data:
        res = eval_map(
            template, datum, pattern
        )
        result.append(res)
    return result


def eval_include(string, data):
    global pattern
    return re.sub(pattern, data, string)
