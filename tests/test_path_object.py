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

    # ------------ Testing define data  ------------
    def test_set_simple_data_as_dict(self):
        self.user_path['testing'] = '123'
        assert self.user_path['testing'].get_value() == '123'

    def test_set_data_from_path_as_dict(self):
        self.user_path['userData.address.extraInfo'] = 'under the stairs'
        assert self.user_path['userData']['address']['extraInfo'].get_value() == 'under the stairs'

    def test_set_data_from_path_with_attributes_as_dict(self):
        self.user_path['$.userData.address.extraInfo'] = 'under the stairs'
        assert self.user_path['userData']['address']['extraInfo'].get_value() == 'under the stairs'

    def test_set_multiple_data_levels_from_path_with_attributes_as_dict(self):
        self.user_path['super.test.creating.multiples.dict.levels'] = "it workds"
        assert self.user_path['super']['test']['creating']['multiples']['dict']['levels'].get_value() == "it workds"

    def test_update_filtered_object_and_check_its_value(self):
        self.user_path.filter.path_contains('price').update_all('999.99')

        for path in self.user_path.get_all_paths():
            if 'price' not in path:
                continue
            object = parse(path).find(self.user_path.get_value())[0]
            assert object.value == '999.99'

    # ----------- Testing retrieve data  -----------

    def test_get_simple_data_from_dict(self):
        assert self.user_path['unique_info'].get_value() == "right info"

    def test_get_data_from_dict_using_jsonpath(self):
        assert self.user_path['userData.address.number'].get_value() == 551

    def test_get_data_from_dict_using_jsonpath_attributes(self):
        assert self.user_path['$.userData.address.number'].get_value() == 551

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