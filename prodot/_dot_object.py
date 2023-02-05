from __future__ import annotations
import typing as t
from ._base_object import BaseObject
from jsonpath_ng import parse

class DotObject(BaseObject):
    arrayTypes = [list]
    numberIndexKey = 'n'
    _temp_path = '$'

    def __getattr__(self, name: str) -> DotObject:
            if type(self.main_object) in self.arrayTypes:
                return self._get_array(name)
            return self._get_map(name)
        
    def __setattr__(self, name: str, value: t.Any) -> None:
        if name in dir(self):
            return super().__setattr__(name, value)

        if name == 'main_object':
            self.__dict__[name] = value
            return

        if self._temp_path != '$':

            json_path = self.__treat_path(f'{self._temp_path}.{name}')

            parse(json_path).update_or_create(self.main_object, value)
            return
        
        if type(self.main_object) in self.arrayTypes:
            self._set_array(name, value)
            return
        self._set_map(name, value)
            

    def _get_map(self, name:str) -> DotObject:
        if name in self.main_object:
            return DotObject(self.main_object[name])

        self._temp_path += f'.{name}'
        return self

    def _get_array(self, name:str) -> DotObject:
        name = name.replace(self.numberIndexKey,'')
        try:
            return DotObject(self.main_object[int(name)])
        except IndexError:
            raise Exception(f"Array index doesn't exist in DotObject {self.true_repr()}")
    
    def _set_map(self, name:str, value:t.Any):
        self.main_object[name] = value

    def _set_array(self, name:str, value:t.Any):
        name = name.replace(self.numberIndexKey,'')
        self.main_object.insert(int(name), value)

    def __treat_path(self, path):
        path_list = []
        for i in path.split('.'):
            if i[0] == 'n' and i[1:].isnumeric():
                path_list.append(f'[{i[1:]}]')
            else:
                path_list.append(i)

        return '.'.join(path_list)

    