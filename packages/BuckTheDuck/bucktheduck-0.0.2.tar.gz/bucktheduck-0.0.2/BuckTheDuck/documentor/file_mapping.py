from dataclasses import dataclass
from typing import List


@dataclass
class Method:
    name: str
    arguments: List[str]
    return_type: str
    start_line: int
    end_line: int
    method_content: str


@dataclass
class FileMapping:
    class_name: str
    public_methods: List[Method]
    private_methods: List[Method]
