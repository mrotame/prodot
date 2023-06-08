from prodot._base_object import BaseObject
from pytest import fixture
from tests.conftest import update_main_object_string
class TestBaseObject:
    def test_temp_scope_and_check_if_no_change_maintain_after_exit_context(self):
        myObject = BaseObject({'test':'hello'})
        with myObject.scoped as temp_obj:
            temp_obj.main_object['foo'] = 'bar'
        
        assert 'foo' not in myObject.main_object

    def test_temp_scope_and_check_if_temp_obj_changes_in_context(self):
        myObject = BaseObject({'test':'hello'})
        with myObject.scoped as temp_obj:
            temp_obj.main_object['foo'] = 'bar'
        assert myObject.get_value() != temp_obj.get_value()

    def test_if_changes_keep_altering_from_external_function(self):
        myObject = BaseObject('hello')
        update_main_object_string(myObject)
        assert myObject.main_object == 'updated_by_external_function'

    def test_list_next_iter(self):
        item_list = ['a','b','c']
        myObject = BaseObject(item_list)
        c = 0
        for letter in myObject:
            assert letter in item_list
            c += 1

        assert c == len(item_list)

    def test_dict_next_iter(self):
        item_list = {'a':10,'b':45,'c':65}
        myObject = BaseObject(item_list)

        for letter in myObject:
            assert item_list[letter] == myObject.main_object[letter]