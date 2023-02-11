import typing as t
from pytest import fixture
from prodot.json_tools import Filter
from prodot import PathObject
from prodot.json_tools._filter import FilteredObject
from jsonpath_ng import parse

class TestFilter:
    @fixture(autouse=True)
    def setup(self, user_info:t.Dict[str,any]):
        self.user = user_info

    @property
    def user_path(self): 
        return PathObject(self.user)

    def test_filter_return_dict_when_filtered_without_class(self):
        filtered_dict = Filter(self.user).path_contains('shoppingCart')
        assert isinstance(filtered_dict, dict)

    def test_filter_return_FilteredObject_object_when_filtered_without_class(self):
        filtered_dict = Filter(self.user, self.user_path).path_contains('shoppingCart')
        assert isinstance(filtered_dict, FilteredObject)

    def test_find_all_paths_with_productName_on_path_and_get_only_filtered_object(self):
        filtered_product_name = Filter(self.user_path.main_object, self.user_path).path_contains('productName')

        assert filtered_product_name.get_filteredObject().get_value() == {
            "shoppingCart" : [{"productName":"notebook",},
            {"productName":"hamtung smartphone",}]}

    def test_find_all_paths_with_productName_on_path_and_update_its_value(self):
        filtered_product_name = Filter(self.user_path.main_object, self.user_path).path_contains('productName').update_all("123")

        for path in self.user_path.get_all_paths():
            if 'productName' not in path:
                continue
            object_value = parse(path).find(self.user_path.get_value())[0].value
            assert object_value == '123'




