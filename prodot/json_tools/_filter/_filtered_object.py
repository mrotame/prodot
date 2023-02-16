from jsonpath_ng import parse



class FilteredObject:
    '''
    The filtered Object is a temporary object returned by
    the filter. This object can be used to manipulate the 
    original BaseObject children after filtering it.
    '''
    def __init__(self, cls, json, filtered_paths):
        self.cls = cls
        self.filtered_json = json
        self.filtered_paths = filtered_paths
        self.filtered_keys = [i.value for path in filtered_paths for i in parse(path).find(json)]

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
        self.cls.main_object = self.filtered_json
        return self.cls