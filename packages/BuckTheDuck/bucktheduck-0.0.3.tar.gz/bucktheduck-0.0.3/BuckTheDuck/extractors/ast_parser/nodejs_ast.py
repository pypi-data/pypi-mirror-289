from dataclasses import dataclass
from typing import List


@dataclass
class Argument:
    name: str
    ts_type: str



@dataclass
class NodejsMethod:
    name: str
    arguments: List[Argument]
    return_type: str
    start_line: int
    end_line: int
    is_async: bool


@dataclass
class NodejsAst:
    class_name: str
    properties: List[Argument] = None
    methods: List[NodejsMethod] = None

    def add_property(self, name, ts_type):
        class_property = Argument(name, ts_type)
        self.properties.append(class_property)

    def add_method(self, name, raw_arguments, return_type, start_line, end_line, is_async):
        arguments = []
        for raw_argument in raw_arguments:
            arguments.append(Argument(raw_argument['name'], raw_argument['type']))
        method = NodejsMethod(name, arguments, return_type, start_line, end_line, is_async)
        self.methods.append(method)