def unique_in_order(iterable):
    unique_list = []
    previous_item = ""
    for item in iterable:
        if item != previous_item:
            unique_list.append(item)
        previous_item = item
    return unique_list
