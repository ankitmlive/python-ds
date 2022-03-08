
def listToString(input_list):
    new_str = ""

    if not input_list:
        return new_str

    for list_element in input_list:
        new_str += list_element
    
    return new_str
