from pytest import fixture
import typing as t
from prodot._dot_object import DotObject

class TestDotObject:
    @fixture(autouse=True)
    def setup(self, user_info:t.Dict[str,any]):
        self.user = user_info

    @property
    def user_dot(self): 
        return DotObject(self.user)

    # ------------ Testing define data  ------------
    def test_set_new_string_and_validate_data(self):
        info = 100
        self.user_dot.new_info = info
        assert self.user_dot.new_info == 100

    def test_set_new_empty_dict_and_insert_data_into_it(self):
        self.user_dot.new_dict = {}
        self.user_dot.new_dict.name = "testing"
        assert self.user_dot.new_dict.name == "testing"

    def test_set_new_filled_dict_and_check_its_data(self):
        self.user_dot.new_dict = {"name":"testing", "value":100}
        assert self.user_dot.new_dict.value == 100

    def test_set_new_list_and_check_information(self):
        self.user_dot.new_array = ["a","b","c'"]
        assert self.user_dot.new_array.n1 == "b"

    def test_set_new_list_add_new_value_and_check_information(self):
        self.user_dot.new_array = ["a","b","c'"]
        self.user_dot.new_array.n3 = "d"
        assert self.user_dot.new_array.n3 == "d"

    def test_set_new_list_replace_value_and_check_information(self):
        self.user_dot.new_array = ["a","b","c'"]
        self.user_dot.new_array.n0 = "da"
        assert self.user_dot.new_array.n0 == "da"

    def test_append_data_to_list_type_dotObject(self):
        self.user_dot.list = []
        self.user_dot.list.append('test')
        assert self.user_dot.list == ['test']

    # ----------- Testing retrieve data  -----------

    def test_check_if_dotObject_path_retrieve_correct_result(self):
        assert self.user_dot.userData.address.street == self.user['userData']['address']['street']

    def test_check_if_str_conversion_retrieve_correct_value(self):
        assert str(self.user_dot.userData.address.street) == self.user['userData']['address']['street']

    def test_check_if_dotObject_path_retrieve_list_index(self):
        assert self.user_dot.shoppingCart.n0.price == self.user['shoppingCart'][0]['price']

    def test_append_data_to_list_type_dotObject(self):
        self.user_dot.list = []
        self.user_dot.list.append('test')

        assert self.user_dot.list == DotObject(['test'])
        
        
    