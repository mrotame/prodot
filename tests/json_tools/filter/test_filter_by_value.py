import typing as t
from pytest import fixture
from prodot.json_tools import Filter
from prodot import PathObject
from prodot.json_tools._filter import FilteredObject
from jsonpath_ng import parse

class TestFilterByValue:
    @fixture(autouse=True)
    def setup(self, user_info:t.Dict[str,any]):
        self.user = user_info

    @property
    def user_path(self): 
        return PathObject(self.user)
    
    def test_filter_return_dict_when_filtered_without_class(self):
        filtered_dict = Filter(self.user).by_value.contains(30)
        assert isinstance(filtered_dict, dict)

    def test_filter_return_FilteredObject_object_when_filtered_with_class(self):
        filtered_dict = Filter(self.user, self.user_path).by_value.contains('Pythonland')
        assert isinstance(filtered_dict, FilteredObject)

    def test_find_all_paths_with_int_9_on_value_and_get_only_filtered_object(self):
        filtered_json = Filter(self.user_path.main_object, self.user_path).by_value.contains('9')
        assert filtered_json.get_filteredObject().get_value() == {'shoppingCart': [{'price': '1499.99'}, {'price': '899.99'}]}

    def test_find_all_paths_with_9_on_value_and_update_its_value(self):
        filtered_json: PathObject = Filter(self.user_path.main_object, self.user_path).by_value.contains(9).update_all(59.99)

        assert len([i['price'] for i in filtered_json.get_value()['shoppingCart'] if i['price'] == 59.99]) == 2

    def test_find_all_paths_with_specific_dict_on_value_and_update_its_value(self):
        filtered_json: PathObject = Filter(self.user_path.main_object, self.user_path).by_value.contains({"important.information": True}).update_all({"test":"test"})

        assert filtered_json['userData'].get_value() == {'test': 'test', 'additionalInformation': {'test': 'test'}}
        
    def test_find_all_paths_where_value_matches_True(self):
        filtered_json = Filter(self.user_path.main_object, self.user_path).by_value.matches(True)

        assert filtered_json.filtered_json == {'userData': {'account_active': True, 'additionalInformation': {'important.information': True}}}

    def test_find_all_paths_where_value_matches_True_and_update_to_False(self):
        updated_json: PathObject = Filter(self.user_path.main_object, self.user_path).by_value.matches(True).update_all(False)

        assert updated_json.filter.by_value.matches(False).filtered_json == {'userData': {'account_active': False, 'additionalInformation': {'important.information': False}}}
        
    