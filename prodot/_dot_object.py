from __future__ import annotations
import typing as t
from ._base_object import BaseObject
from jsonpath_ng import parse

class DotObject(BaseObject):
    '''
    ## Description
    The dot object gives the maps and arrays more power
    by let you treat the object like a common class.
    All values can be accessed by this method.


    ## Parameters
    `main_object:` a Dict or List object that will be interpreted
    by the children objects
    '''
    arrayTypes = [list]
    numberIndexKey = 'n'

    def __getattr__(self, name: str) -> t.Self:
        if type(self.main_object) in self.arrayTypes:
            res = self._get_array(name)
        else:
            res = self._get_map(name)

        if isinstance(res, list) or isinstance(res, dict):
            return self.__class__(res, maintain=True)
        return res
        
    def __setattr__(self, name: str, value: t.Any) -> None:
        if name in dir(self):
            return super().__setattr__(name, value)

        if name == 'main_object':
            self.__dict__[name] = value
            return

        if type(self.main_object) in self.arrayTypes:
            self._set_array(name, value)
            return
        self._set_map(name, value)
            
    def _get_map(self, name:str) -> t.Any:
        if name in self.main_object:
            return self.main_object[name]

        raise ValueError(f"Key <<{name}>> not found in  the main_object")

    def _get_array(self, name:str) -> t.Any:    
        if name.startswith(self.numberIndexKey):
            name = name.replace(self.numberIndexKey,'')
        try:
            return self.main_object[int(name)]
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

    