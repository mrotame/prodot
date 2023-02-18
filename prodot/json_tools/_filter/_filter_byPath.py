import typing as t
from .. import get_all_paths
from jsonpath_ng import parse
from ._filtered_object import FilteredObject

class FilterByPath:
    def __init__(self, json, cls):
        self.cls = cls
        self.json = json
        self.filtered_json = dict()
        self.filtered_paths = list()

    def contains(self, string_to_search:str)->FilteredObject:
        '''
        Check for each possible json path in the received json object
        and returns a FilteredObject containing all the possible
        json paths that contains the string parameter anywhere
        in the path
        '''
        for path in get_all_paths(self.json):
            if string_to_search in path:
                self.filtered_paths.append(path)
                path = parse(path)
                path.update_or_create(self.filtered_json, path.find(self.json)[0].value)
                
        return self.__define_return(self.filtered_json)

    def endswith(self, string_to_search:str)->FilteredObject:
        for path in get_all_paths(self.json):
            if f'"{string_to_search}"' == path.split('.')[-1]:
                self.filtered_paths.append(path)
                path = parse(path)
                path.update_or_create(self.filtered_json, path.find(self.json)[0].value)
                
        return self.__define_return(self.filtered_json)

    def __define_return(self, json:t.Dict[str,t.Any]={}):
        
        if self.cls:
            return FilteredObject(self.cls, json, self.filtered_paths)
        return json