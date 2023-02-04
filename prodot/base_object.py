import typing as t

class BaseObject:
    main_object: t.Dict

    def __init__(self, main_object: t.Union[t.Dict,None]= dict()):
        self.main_object = main_object

    def __repr__(self) -> t.Dict:
        return str(self.main_object)
        
    def true_repr(self)-> str:
        type_ = type(self)
        module = type_.__module__
        qualname = type_.__qualname__
        return f"<{module}.{qualname} object at {hex(id(self))}>"

    def __str__(self)-> str:
        return self.main_object

    def get_value(self):
        return self.main_object