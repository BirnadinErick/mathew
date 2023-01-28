import re
from types import FunctionType
from datastore import DataStore


class TemplateEngine:
    pattern = r'{\s?(\w+)\s?}'

    def __init__(self):
        pass

    def parse(self, template: str, get_data: FunctionType) -> str:
        """
        parses a given template string using get_data
        """
        return re.sub(self.pattern, get_data, template)
