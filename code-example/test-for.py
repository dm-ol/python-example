#

my_dict = {"key1": True, "key2": 2, "key3": 42}


def dict_to_list(convert_dict):
    my_list = []
    for key, value in convert_dict.items():
        if type(value) == int:
            value *= 2
        my_list.append((key, value))
    return my_list


print(dict_to_list(my_dict))
