from __future__ import annotations
import typing as t
from .base_object import BaseObject

class DotObject(BaseObject):
    arrayTypes = [list]

    def __getattr__(self, name: str) -> DotObject:
        if type(self.main_object) in self.arrayTypes:
            return self._get_array(name)
        return self._get_map(name)
        
    def __setattr__(self, name: str, value: t.Any) -> None:
        if name == 'main_object':
            self.__dict__[name] = value
            return
        
        if type(self.main_object) in self.arrayTypes:
            self._set_array(name, value)
            return
        self._set_map(name, value)
            

    def _get_map(self, name:str) -> DotObject:
        if name in self.main_object:
            return DotObject(self.main_object[name])
        else:
            raise Exception(f"Key doesn't exist in DotObject {self.true_repr()}")

    def _get_array(self, name:str) -> DotObject:
        name = name.replace('n','')
        try:
            return DotObject(self.main_object[int(name)])
        except IndexError:
            raise Exception(f"Array index doesn't exist in DotObject {self.true_repr()}")
    
    def _set_map(self, name:str, value:t.Any):
        self.main_object[name] = value

    def _set_array(self, name:str, value:t.Any):
        name = name.replace('n','')
        self.main_object.insert(int(name), value)
    