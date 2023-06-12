import typing as t
from pytest import fixture
from prodot._path_object import PathObject
from jsonpath_ng import parse

class TestPathObject:
    @fixture(autouse=True)
    def setup(self, user_info:t.Dict[str,any]):
        self.user = user_info

    @property
    def user_path(self): 
        return PathObject(self.user)
    
    @property
    def object(self):
        return PathObject

    # ------------ Testing define data  ------------
    def test_set_simple_data_as_dict(self):
        self.user_path['testing'] = '123'
        assert self.user_path['testing'] == '123'

    def test_set_data_from_path_as_dict(self):
        self.user_path['userData.address.extraInfo'] = 'under the stairs'
        assert self.user_path['userData']['address']['extraInfo'] == 'under the stairs'

    def test_set_data_from_path_with_attributes_as_dict(self):
        self.user_path['$.userData.address.extraInfo'] = 'under the stairs'
        assert self.user_path['userData']['address']['extraInfo'] == 'under the stairs'

    def test_set_multiple_data_levels_from_path_with_attributes_as_dict(self):
        self.user_path['super.test.creating.multiples.dict.levels'] = "it workds"
        assert self.user_path['super']['test']['creating']['multiples']['dict']['levels'] == "it workds"

    def test_update_filtered_object_and_check_its_value(self):
        self.user_path.filter.by_path.contains('price').update_all('999.99')
        
        for path in self.user_path.get_all_paths():
            if 'price' not in path:
                continue
            object = parse(path).find(self.user_path.get_value())[0]
            assert object.value == '999.99'

    def test_append_data_to_list_type_PathObject(self):
        self.user_path['list'] = []
        self.user_path['list'].append('test')
        assert self.user_path['list'].get_value() == ['test']

    def test_create_path_object_with_num_as_key(self):
        path = PathObject()
        path[10] = True
        assert path[10]

    # ----------- Testing retrieve data  -----------

    def test_assert_key_in_object(self):
        assert ("unique_info" in self.user_path) == True

    def test_check_undefined_key_not_in_object(self):
        assert ('foo' not in self.user_path) == True

    def test_get_simple_data_from_dict(self):
        assert self.user_path['unique_info'] == "right info"

    def test_get_data_from_dict_using_jsonpath(self):
        assert self.user_path['userData.address.number'] == 551

    def test_get_data_from_dict_using_jsonpath_attributes(self):
        assert self.user_path['$.userData.address.number'] == 551

    def test_get_all_json_paths_from_dict(self):
        custom_dict = {
            "testing":"hello",
            "foo":{"bar":"eggs"},
            "foo_array" : [{"bar":"eggs"},{"foo":"bar"}]
        }
        myObject = PathObject(custom_dict)
    
        assert list(myObject.get_all_paths()) == \
            [
                '$."testing"', '$."foo"', '$."foo"."bar"', '$."foo_array"', 
                '$."foo_array"[0]', '$."foo_array"[0]."bar"', 
                '$."foo_array"[1]', '$."foo_array"[1]."foo"'
            ]
        
    def test_append_data_to_list_type_PathObject(self):
        self.user_path['list'] = []
        self.user_path['list'].append('test')
        assert self.user_path['list'] == PathObject(['test'])

    def test_new_path_object_does_not_return_existent_one(self):
        new_object = self.object()
        new_object['test'] = True
        empty_object = self.object()

        assert new_object != empty_object