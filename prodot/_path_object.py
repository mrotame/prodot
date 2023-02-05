from __future__ import annotations
import typing as t
from ._base_object import BaseObject
from jsonpath_ng.ext import parse

class PathObject(BaseObject):

    def __getitem__(self, name:str)->PathObject:
        try:
            return PathObject(parse('$.'+name).find(self.main_object)[0].value)
        except IndexError:
            raise Exception(f"path <<{name}>> not found at the main_object")

    def __setitem__(self, name:str, value:t.Any):
        path = parse('$.'+name)
        path.update_or_create(self.main_object, value)

    def get_all_paths(self, **kwargs)->t.Iterable:
        if not kwargs.get('dict_to_get_path', dict()):
            dict_to_get_path = self.main_object
        else:
            dict_to_get_path = kwargs['dict_to_get_path']

        if isinstance(dict_to_get_path, dict):
            for key, value in dict_to_get_path.items():
                yield f'.{key}'
                yield from (f'.{key}{p}' for p in self.get_all_paths(dict_to_get_path=value))
            
        elif isinstance(dict_to_get_path, list):
            for i, value in enumerate(dict_to_get_path):
                yield f'[{i}]'
                yield from (f'[{i}]{p}' for p in self.get_all_paths(dict_to_get_path=value))
