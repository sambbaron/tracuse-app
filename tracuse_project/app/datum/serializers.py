

def datum_object_element_expr(datum_object):
    """Return elements for expression evaluation

    Returns:
        Dictionary:
            Key: element_type.schema_name
            Value: element_value.elvalue
    """
    output = {}

    for element in datum_object.elements:
        element_name = element.element_type.schema_name
        element_value = element.element_value
        if element_value:
            output[element_name] = element_value.elvalue

    return output


