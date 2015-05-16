import json
from django.core.serializers.json import DjangoJSONEncoder

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


def datum_serializer(datum_object):

    parent_datums = [parent_datum.datum_object_id for parent_datum in datum_object.all_parent_datums.all()]
    child_datums = [child_datum.datum_object_id for child_datum in datum_object.all_child_datums.all()]

    output = {
        "datum_object_id": datum_object.datum_object_id,
        "datum_type_id": datum_object.datum_type_id,
        "parent_datums": parent_datums,
        "child:datums": child_datums,
        "element": datum_object_element_expr(datum_object)
    }
    return output

def serialize_datums():
    from app.datum.models import DatumObject
    output = []
    for datum_object in DatumObject.objects.all():
        output.append(datum_serializer(datum_object))
    return json.dumps(output,
                      cls=DjangoJSONEncoder,
                      indent=4
                      )

