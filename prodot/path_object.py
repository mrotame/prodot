import typing as t
from .pro_object import ProObject
from jsonpath_ng.ext import parse

class PathObject(ProObject):

    def __getitem__(self, name:str)->t.Any:
        try:
            return parse('$.'+name).find(self.main_object)[0].value
        except IndexError:
            raise Exception(f"path <<{name}>> not found at the main_object")

    def __setitem__(self, name:str, value:t.Any):
        path = parse('$.'+name)
        path.update_or_create(self.main_object, value)

    def all_paths_from_main_object(self, **kwargs)->t.Iterable:
        if not kwargs.get('dict_to_get_path', dict()):
            dict_to_get_path = self.main_object
        else:
            dict_to_get_path = kwargs['dict_to_get_path']

        if isinstance(dict_to_get_path, dict):
            for key, value in dict_to_get_path.items():
                yield f'.{key}'
                yield from (f'.{key}{p}' for p in self.all_paths_from_main_object(dict_to_get_path=value))
            
        elif isinstance(dict_to_get_path, list):
            for i, value in enumerate(dict_to_get_path):
                yield f'[{i}]'
                yield from (f'[{i}]{p}' for p in self.all_paths_from_main_object(dict_to_get_path=value))
