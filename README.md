# Prodot

A new way to deal with dictionaries and lists in python.
Treat data like classes, or by reading/writing data with json paths

# Getting started

## install
```
pip install prodot
```

## Usage

Import the pro object from the prodot library. You can create a new empty dictionary, or start with a filled one

```Python
from prodot import ProObject

# No parameters instances an empty dictionary
my_new_obj = ProObject() 

# The pro object can be initialized with a dictionary
my_dict_obj = ProObject({"foo":["bar,"eggs"]})

# The pro object can also initialize with a list
my_list_obj = ProObject([ [1,2,3], ["a","b","c"], [{"foo":"bar"}, {"bar":"eggs"}] ])

```

### Dot notation usage
By using the pro-object you can use the dictionary as a class

```Python
my_json = {
  "userData": {
    "name": "John",
    "age": "38",
    "shoppingCart": [
      {"cellphone": 999.99},
      {"notebook": 2999.99},
      {"wireless keyboard": 299.99}
    ]
  }
}

my_new_obj = ProObject(my_json)

shoppingCart = my_new_obj.userData.shoppingCart
```

The ProObject will return another instance of the ProObject with the main_object attribute as being the selected path.

```Python
>>> type(shoppingCart)
<class 'prodot.pro_object.ProObject'>
```

To get the raw value of the object, you can use the `.get_value()` function.

```Python
>>> shoppingCart.get_value()
[{"cellphone": 999.99}, {"notebook": 2999.99}, {"wireless keyboard": 299.99}]

# or by using the get_value directly at the path
>>> my_new_obj.userData.shoppingCart.get_value()
[{"cellphone": 999.99}, {"notebook": 2999.99}, {"wireless keyboard": 299.99}]

>>> type(shoppingCart.get_value())
<class 'dict'>
```

You can also add new information to the instancied object

```Python
# n3 means list index 3 (will be added as 4th item)
>>> my_new_obj.userData.shoppingCart.n3 = {"monitor": 699.99}
>>> my_new_obj.userData.shoppingCart.get_value()
[{"cellphone": 999.99}, {"notebook": 2999.99}, {"wireless keyboard": 299.99}, {"monitor": 399.99}]
```
Python doesn't accept list indexes to be used as a class attribute. For solve this problem, list indexes start with the `n` letter (like n0, n1, ...)

### Json path usage

If you prefere or need to use json paths, it is possible to write and retrieve information using json path strings.

```Python
>>> my_new_obj['$.userData.shoppingCart[4]'] = {'FunStation 6 Series T':'699,99'}

>>> my_new_obj['$.userData.shoppingCart'].get_value()
[{"cellphone": 999.99}, {"notebook": 2999.99}, {"wireless keyboard": 299.99}, {"monitor": 399.99}, {'FunStation 6 Series T':'699,99'}]
```

Note that by using a json path string, list indexes must not have `n` as their first value.

You can view all possible json_paths from object by using the `get_all_paths` attribute.

```Python
>>> my_new_obj.get_all_paths()
<generator object PathObject.all_paths_from_main_object at 0x7f6a012b5c80>

>>> list(my_new_obj.get_all_paths())
['.userData', '.userData.name', '.userData.age', '.userData.shoppingCart', '.userData.shoppingCart[0]', '.userData.shoppingCart[0].cellphone', '.userData.shoppingCart[1]', '.userData.shoppingCart[1].notebook', '.userData.shoppingCart[2]', '.userData.shoppingCart[2].wireless keyboard', '.userData.shoppingCart[3]', '.userData.shoppingCart[3].monitor', '.userData.shoppingCart[4]', '.userData.shoppingCart[4].FunStation 6 Series T']
```

