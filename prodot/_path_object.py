from __future__ import annotations
import typing as t
from ._base_object import BaseObject
from jsonpath_ng.ext import parse
from .json_tools import get_all_paths

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
        return get_all_paths(self.main_object, **kwargs)
