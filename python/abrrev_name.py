def abbrev_name(name):
    name = name.uppercase
    last_name = (name.find(' '))+1
        
    return name[0] + last_name[0]