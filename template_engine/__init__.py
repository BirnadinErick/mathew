import re
from types import FunctionType
from datastore import DataStore

temp_buffer = []


class TemplateEngine:
    pattern = r'{\s?(\w+)\s?}'
    pattern_v2 = r'{\s?\w+\s(\w+.\w+)\s?}'

    def __init__(self, templates_dir: str):
        self.templates_dir = templates_dir

    def parse(self, template: str, get_data: FunctionType) -> str:
        """
        parses a given template string using get_data
        """
        return re.sub(self.pattern, get_data, template)

    # def __include_many(match) -> str:
    #     global temp_buffer
    #     keys = match.group(1).split(".")
    #     tbl, col = keys[0], keys[1]
    #     return temp_buffer[tbl][col]

    # def _include_many(self, file: str, data) -> str:
    #     global temp_buffer

    #     for datum in data:
    #         temp_buffer = datum

    #         with open(self.templates_dir + file, 'r') as template_file:
    #             result = re.sub(
    #                 self.pattern,
    #                 self.__include_many,
    #                 template_file.read()
    #             )
    #             print(result)
    #             return result
    def eval_map(self, string, data, pattern):
        parsed = re.sub(
            pattern, lambda m: data[m.group(1).split(".")[1]], string
        )
        return parsed

    def parse_template(self, template, data):
        result = []
        for datum in data:
            res = eval_map(
                template, datum, self.pattern_v2
            )
            result.append(res)
        return result

    def eval_include(self, string, data):
        global pattern
        return re.sub(pattern, data, string)
