import typing as t
from abc import ABC, abstractmethod
import copy
from contextvars import ContextVar

class BaseObject(ABC):
    '''
    ## Description
    A base object to be used by all other object types (like the dot object and the path object). This abstract class has the basic and common configuration for all the future object classes

    ## Parameters
    `main_object:` a Dict or List object that will be interpreted
    by the children objects
    '''
    
    
    '''The main object is the object that the class will be representing (most times, it will be a list or a dictionary)'''   
    main_object: t.Any

    @property
    def scoped(self):
        '''
        Return the Object as a temporary object to be used within a scope. Ex:
        ```Python
        >> with my_obj.scoped as temp_object:
        >> ... print( temp_object.get_value() )
        ```
        '''
        class Scope:
            def __init__(self, caller: BaseObject, main_object:t.Any):
                self.caller = caller
                self.main_object = main_object

            def __enter__(self):
                return copy.deepcopy(self.caller.__class__(self.main_object))
                
            def __exit__(self, exc_type, exc_value, traceback):
                pass

        return Scope(self, self.main_object)

    def __contains__(self, value: str)-> t.Any:
        if value in self.main_object:
            return True
        return False

    def __init__(self, main_object: t.Union[t.Dict, t.List, None] = {}, *args, **kwargs):
        '''
        The init will receive the main object as parameter, 
        or will create an initialize with an empty dictionary
        '''
        if main_object or kwargs.get('maintain'):
            self.main_object = main_object
        elif isinstance(main_object, list):
            self.main_object = list()
        else:
            self.main_object = dict()

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

    def __eq__(self, __value: object) -> bool:
        return __value == self.main_object

    def get_value(self):
        '''
        Returns the content inside of the main_object
        '''
        return self.main_object
    
    def append(self, value: t.Any):
        '''
        Append the value if the main_object is a list
        '''
        return self.main_object.append(value)
    
    def __iter__(self):
        return iter(self.main_object)