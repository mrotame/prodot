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
      {"cellphone": 999.99}
      {"notebook": 2999.99}
      {"wireless keyboard": 299.99}
    ]
  }
}

my_new_obj = DotObject(my_json)

shoppingCart = my_new_obj.userData.shoppingCart
```