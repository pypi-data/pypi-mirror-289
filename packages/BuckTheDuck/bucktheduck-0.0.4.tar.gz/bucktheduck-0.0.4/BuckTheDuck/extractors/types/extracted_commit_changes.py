from dataclasses import dataclass
from enum import Enum
from typing import List


class MethodStatus(Enum):
    ADDED = 'added'
    REMOVED = 'removed'
    EDITED = 'edited'

@dataclass
class ClassProperties:
    name: str
    type: str

@dataclass
class MethodMapping:
    method_name: str
    status: MethodStatus

    def __str__(self):
        return f'{self.method_name} - {self.status.value}'


@dataclass
class ChangeMapping:
    class_name: str
    method_name: List[MethodMapping]
    properties: List[ClassProperties] = None

    def __str__(self):
        change_mapping_str = f'Class Name: {self.class_name}'
        if self.properties:
            change_mapping_str += ', class properties: '
            for property in self.properties:
                change_mapping_str += f'{property.name} type {property.type}'
        change_mapping_str += ', methods: '
        for method in self.method_name:
            change_mapping_str += f'{method},'
        return change_mapping_str[:-1]


@dataclass
class ExtractedCommitChanges:
    files_changed: List[ChangeMapping]
    files_added: List[ChangeMapping]
    files_removed: List[str]

    def add_changes(self, change_mapping: List[ChangeMapping]):
        self.files_changed += change_mapping

    def add_new_changes(self, change_mapping: List[ChangeMapping]):
        self.files_added += change_mapping

    def add_removed_class(self, removed_class_name: List[str]):
        self.files_removed += removed_class_name
