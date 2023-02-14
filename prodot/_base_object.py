import typing as t
from abc import ABC
class BaseObject(ABC):
    '''
    ## Description
    A base object to be used by all other object types (like the dot object and the path object). This abstract class has the basic and common configuration for all the future object classes

    ## Parameters
    `main_object:` a Dict or List object that will be interpreted
    by the children objects
    '''
 
    def main_object(self)-> t.Any:
        '''
        The main object is the object that the class will be representing (most times, it will be a list or a dictionary)
        '''
    
    def __init__(self, main_object: t.Union[t.Dict, t.List, None] = dict()):
        '''
        the init will receive the main object as parameter, 
        or will create an initialize with an empty dictionary
        '''
        self.main_object = main_object

    def __repr__(self) -> t.Dict:
        return str(self.main_object)
    
    def true_repr(self)-> str:
        '''
        returns the original representation of the base
        object.
        '''
        type_ = type(self)
        module = type_.__module__
        qualname = type_.__qualname__
        return f"<{module}.{qualname} object at {hex(id(self))}>"

    def __str__(self)-> str:
        return str(self.main_object)

    def get_value(self):
        '''
        returns the content inside of the main_object
        '''
        return self.main_object