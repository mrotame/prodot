from __future__ import annotations

import typing as t
from . import get_all_paths
from jsonpath_ng import parse

if t.TYPE_CHECKING:
    from prodot import PathObject

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
            
    def path_contains(self, string_to_search:str)->FilteredObject:
        '''
        Check for each possible json path in the received json object
        and returns a FilteredObject containing all the possible
        json paths that contains the string parameter anywhere
        in the path
        '''
        filtered_json = {}
        filtered_paths = []
        for path in get_all_paths(self.json):
            if string_to_search in path:
                filtered_paths.append(path)
                
                path = parse(path)
                path.update_or_create(filtered_json, path.find(self.json)[0].value)
                
        return self.define_return(filtered_json, filtered_paths)

    def define_return(self, json:t.Dict[str,t.Any]={}, filtered_paths:t.List[str]=[]):
        
        if self.cls:
            return FilteredObject(self.cls, json, filtered_paths)
        return json
        
class FilteredObject:
    '''
    The filtered Object is a temporary object returned by
    the filter. This object can be used to manipulate the 
    original BaseObject children after filtering it.
    '''
    def __init__(self, cls, json, filtered_paths):
        self.cls = cls
        self.json = json
        self.filtered_paths = filtered_paths

    def update_all(self, value):
        '''
        Update all filtered data to a new value
        '''
        for path in self.filtered_paths:
            path = parse(path)
            path.update_or_create(self.cls.main_object, value)
        return self.get_object()

    def get_object(self):
        '''
        Returns the original BaseObject children Object
        without any manipulation
        '''
        return self.cls

    def get_filteredObject(self):
        '''
        Returns the original BaseObject children Object with
        the main_object attribute containing only the filtered data
        '''
        self.cls.main_object = self.json
        return self.cls