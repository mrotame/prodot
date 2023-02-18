from __future__ import annotations

import typing as t
from ._filter_byPath import FilterByPath
from ._filter_byValue import FilterByValue
class Filter:
    '''
    ## Description
    The `Filter` Object can be used to find data across the entire object. Right now it is lacking in functionality. 
    More ways to search data will be implemented in the future

    ## Parameters
    `json:` An map or array that will be searched.
    `cls:` An optional parameter that receives a BaseObject children
        if a cls is passed, the filter will be returned as a
        FilteredObject instead of the raw filtered json
    '''
    def __init__(self, json:t.Dict[str,t.Any] | t.List, cls=None):
        self.json = json
        self.cls = cls
        self.__filterByPath = FilterByPath
        self.__filterByValue = FilterByValue

    @property
    def by_path(self):
        return self.__filterByPath(self.json, self.cls)
    
    @property
    def by_value(self):
        return self.__filterByValue(self.json, self.cls)

    
 