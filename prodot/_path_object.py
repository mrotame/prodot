from __future__ import annotations
import typing as t
from ._base_object import BaseObject
from jsonpath_ng.ext import parse
from .json_tools import get_all_paths
from .json_tools import Filter

class PathObject(BaseObject):
    '''
    ## Description
    The Path object gives the user ability to use
    json path to access a json data.
    All values can be accessed by this method.

    John

    ## Parameters
    `main_object:` a Dict or List object that will be interpreted
    by the children objects
    '''
    @property
    def __filter_object(self)->Filter:
        '''
        return the filter object that will be used by the class.
        Overwrite this if you want to use your own filter class
        '''
        return Filter

    @property
    def filter(self)->Filter:
        '''
        returns a filter instance responsible to extract data
        from the main_object
        '''
        return self.__filter_object(self.main_object, self)
        
    def __getitem__(self, name:str)->t.Self:
        try:
            res = parse('$.'+name).find(self.main_object)[0].value
            if isinstance(res, list) or isinstance(res, dict):
                return self.__class__(res)
            return res
    
        except IndexError:
            raise IndexError(f"path <<{name}>> not found in  the main_object")

    def __setitem__(self, name:str, value:t.Any):
        path = parse('$.'+name)
        path.update_or_create(self.main_object, value)

    def get_all_paths(self, **kwargs)->t.Iterable:
        '''
        return an iterable that
        runs across the entire main_object, returning
        all possible json_paths of the object
        '''
        return get_all_paths(self.main_object, **kwargs)