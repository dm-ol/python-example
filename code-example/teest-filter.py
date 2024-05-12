# Filter test (timing 14:45)

def filter_list(list_to_filter, value_type):
    def check_element_type(elem):
        return isinstance(elem, value_type)

    return list(filter(check_element_type, list_to_filter))


print(filter_list([35, True, "eleven", 10], int))
