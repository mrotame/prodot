from pytest import fixture

@fixture
def user_info():
    return {
        "unique_info": "right info",
        "userData": {
            "name": "John Doe",
            "account_active": True,
            "age":30,
            "address": {
                "street":"List Ave",
                "number":551,
                "city":"Pythonland",
            },
            "additionalInformation": {
                "important.information": True
            }
            
        },
        "shoppingCart" : [
            {
                "productName":"notebook",
                "price":"1499.99",
                "id":12345
            },
            {
                "productName":"hamtung smartphone",
                "price":"899.99",
                "id":12345
            }
        ]
    }