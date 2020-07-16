
def extract_id(attr):
    """
    extract id from the attribute
    :params: attr primary key or sort key  
    """
    id = "".join(attr.split("#")[-1])
    return id