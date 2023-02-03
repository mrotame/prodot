import typing as t

class DotObject:
    main_object: t.Dict

    def __init__(self, main_object: t.Union[t.Dict,None]= dict()):
        self.main_object = main_object

    def __repr__(self) -> t.Dict:
        return str(self.main_object)

    def __getattr__(self, name: str) -> t.Any:
        breakpoint()
        if name in self.main_object:
            return DotObject(self.main_object[name])
        else:
            raise Exception(f"Key doesn't exist in DotObject {self.true_repr()}")

    def __setattr__(self, name: str, value: t.Any) -> None:
        if name == 'main_object':
            self.__dict__[name] = value
        else:
            self.main_object[name] = value
        
    def true_repr(self):
        type_ = type(self)
        module = type_.__module__
        qualname = type_.__qualname__
        return f"<{module}.{qualname} object at {hex(id(self))}>"