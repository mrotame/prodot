import typing as t
from pytest import fixture
from prodot.pro_object import ProObject

from .test_dot_object import TestDotObject
from .test_path_object import TestPathObject

class TestProObject(TestDotObject, TestPathObject):
    @property
    def user_dot(self): 
        return ProObject(self.user)

    @property
    def user_path(self): 
        return ProObject(self.user)