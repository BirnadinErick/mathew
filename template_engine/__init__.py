import re
from types import FunctionType
from datastore import DataStore

temp_buffer = []


class TemplateEngine:
    pattern = r'{\s?(\w+)\s?}'

    def __init__(self, templates_dir: str):
        self.templates_dir = templates_dir

    def parse(self, template: str, get_data: FunctionType) -> str:
        """
        parses a given template string using get_data
        """
        return re.sub(self.pattern, get_data, template)

    def __include_many(match) -> str:
        global temp_buffer
        keys = match.group(1).split(".")
        tbl, col = keys[0], keys[1]
        return temp_buffer[tbl][col]

    def _include_many(self, file: str, data) -> str:
        global temp_buffer

        for datum in data:
            temp_buffer = datum

            with open(self.templates_dir + file, 'r') as template_file:
                result = re.sub(
                    self.pattern,
                    self.__include_many,
                    template_file.read()
                )
                print(result)
                return result
