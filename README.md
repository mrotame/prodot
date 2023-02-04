# prodot

A new way to deal with dictionaries and lists in python.

## install
```
pip install prodot
```

## Usage

Import the dot object from the prodot library. You can create a new empty dictionary, or start with a filled one

```Python
from prodot import DotObject

# No parameters instances an empty dictionary
my_new_obj = DotObject() 

# The Dot Object can be initialized with a dictionary
my_dict_obj = DotObject({"foo":["bar,"eggs"]})

# The Dot Object can also initialize with a list
my_list_obj = DotObject([ [1,2,3], ["a","b","c"], [{"foo":"bar"}, {"bar":"eggs"}] ])

```

### Dot notation usage
By using the dot-object you can use the dictionary as a class
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

my_new_obj = DotObject(my_json)

shoppingCart = my_new_obj.userData.shoppingCart
```

The DotObject will return another instance of the DotObject with the main_object attribute as being the selected path.

```Python
>>> type(shoppingCart)
<class 'prodot.dot_object.DotObject'>
```

To get the brute value of the object, you can use the `.get_value()` function.

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
[{"cellphone": 999.99}, {"notebook": 2999.99}, {"wireless keyboard": 299.99}, {"monitor": 699.99}]
```
Python doesn't accept list indexes to be used as a class attribute. For solve this problem, list indexes start with the `n` letter (like n0, n1, ...)

