# First test (Timing 14:25)

my_dict = {"key1": True, "key2": 2, "key3": 42}


def dict_to_list(convert_dict):
    my_list = []
    for key, value in convert_dict.items():
        if type(value) == int:
            value *= 2
        my_list.append((key, value))
    return my_list


print(dict_to_list(my_dict))


# Test 2 (Timing 14:25)

def filter_list(list_to_filter, value_type):
    filtered_list = []
    for element in list_to_filter:
        if type(element) == value_type:
            filtered_list.append(element)
    return filtered_list


print(filter_list([35, True, "eleven", 10], int))

# or with isinstance (not recommended, because bool is subclass int)


def filter_list(list_to_filter, value_type):
    filtered_list = []
    for element in list_to_filter:
        if isinstance(element, value_type):
            filtered_list.append(element)
    return filtered_list


print(filter_list([35, True, "eleven", 10], int))
