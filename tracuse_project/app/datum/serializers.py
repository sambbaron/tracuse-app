

def datum_object_element_expr(datum_object):
    """Return elements for expression evaluation

    Returns:
        Dictionary:
            Key: element_type.schema_name
            Value: element_value.element_value
    """
    output = {}

    elements = datum_object.element_datum_objects.all()

    for element in elements:
        element_name = element.element_type.schema_name
        element_value = element.element_value
        output[element_name] = element_value

    return output


