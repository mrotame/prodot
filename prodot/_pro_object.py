import typing as t
from ._dot_object import DotObject
from ._path_object import PathObject

class ProObject(DotObject, PathObject):
    '''
    ## Description
    The `ProObject` joins the `DotObject` and the `PathObject` into one
    powerful object. Data can be accessed by using both the Dot
    or the Json Path method

    ## Parameters
    `main_object:` a Dict or List object that will be interpreted
    by the children objects
    '''