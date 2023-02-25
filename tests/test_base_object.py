from prodot._base_object import BaseObject

class TestBaseObject:
    def test_base_object_context_and_check_if_no_change_maintain_after_exit_context(self):
        myObject = BaseObject({'test':'hello'})
        with myObject.scoped as temp_obj:
            temp_obj.main_object['foo'] = 'bar'
        
        assert 'foo' not in myObject.main_object

    def test_base_object_context_and_check_if_temp_obj_changes_in_context(self):
        myObject = BaseObject({'test':'hello'})
        with myObject.scoped as temp_obj:
            temp_obj.main_object['foo'] = 'bar'
        assert myObject.get_value() != temp_obj.get_value()
