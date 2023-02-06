import typing as t
from . import get_all_paths
from jsonpath_ng import parse

if t.TYPE_CHECKING:
    from prodot import PathObject

class Filter:
    def __init__(self, json:t.Dict[str,t.Any], cls=None):
        self.json = json
        self.cls = cls
            
    def path_contains(self, s:str):
        filtered_json = {}
        filtered_paths = []
        for path in get_all_paths(self.json):
            if s in path:
                filtered_paths.append(path)
                path = parse(path)
                path.update_or_create(filtered_json, path.find(self.json)[0].value)
                
        return self.define_return(filtered_json, filtered_paths)

    def define_return(self, json:t.Dict[str,t.Any]={}, filtered_paths:t.List[str]=[]):
        
        if self.cls:
            return FilteredObject(self.cls, json, filtered_paths)
        return json
        
class FilteredObject:

    def __init__(self, cls, json, filtered_paths):
        self.cls = cls
        self.json = json
        self.filtered_paths = filtered_paths

    def update_all(self, value):
        for path in self.filtered_paths:
            path = parse(path)
            path.update_or_create(self.cls.main_object, value)
        return self.get_object

    @property
    def get_object(self):
        return self.cls

    @property
    def get_filteredObject(self):
        self.cls.main_object = self.json
        return self.cls