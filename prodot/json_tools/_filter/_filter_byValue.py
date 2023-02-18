import typing as t
from .. import get_all_paths
from jsonpath_ng import parse
from ._filtered_object import FilteredObject

class FilterByValue:
    def __init__(self, json, cls):
        from prodot import PathObject

        self.cls = cls
        self.json = json
        self.filtered_json = dict()
        self.filtered_paths = list()
        self.pathObject = PathObject

    def contains(self, str_to_search:str)->FilteredObject:
        '''
        Check for each possible json path in the received json object,
        compare each value from each path, and returns a FilteredObject
        containing all the possible json paths that contains the data
        parameter anywhere in the value
        '''
        
        for path in get_all_paths(self.json):
            value = self.pathObject(self.json)[path].get_value()
            
            try: str_to_search in value
            except Exception: value = str(value)
            if str(str_to_search) in value:
                self.filtered_paths.append(path)
                path = parse(path)
                path.update_or_create(self.filtered_json, path.find(self.json)[0].value)

        return self.__define_return(self.filtered_json)
    
    def matches(self, data_to_search:any):
        '''
        Check for each possible json path in the received json object,
        compare each value from each path, and returns a FilteredObject
        containing all the possible json paths that the data_to_search matches exactly the value
        '''
        for path in get_all_paths(self.json):
            value = self.pathObject(self.json)[path].get_value()
            try: data_to_search in value
            except Exception: value = str(value)
            if str(data_to_search) == value:
                self.filtered_paths.append(path)
                path = parse(path)
                path.update_or_create(self.filtered_json, path.find(self.json)[0].value)

        return self.__define_return(self.filtered_json)

    
    def __define_return(self, json:t.Dict[str,t.Any]={}):
        
        if self.cls:
            return FilteredObject(self.cls, json, self.filtered_paths)
        return json