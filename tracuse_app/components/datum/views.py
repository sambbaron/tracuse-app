from components.datum.models import DatumObject, DatumType
from components.element_type.models import ElementTypeDatumObject
from components.element_value import models as ElementValueModels


def create_datum_with_elements(user_id, datum_type_id):
    # Create new Datum Object
    new_datum = DatumObject()
    # Assign base Datum Object properties
    new_datum.user_id = user_id
    new_datum.datum_type_id = datum_type_id
    new_datum.save()

    # Get default element types by datum type
    datum_type = DatumType.objects.get(pk=datum_type_id)
    default_element_types = datum_type.element_types.all()

    # Add default element types to object type
    new_elements = []
    for datum_element in default_element_types:
        new_datum_element = ElementTypeDatumObject(datum_object=new_datum,
                                             element_type=datum_element.element_type
                                             )
        new_datum_element.save()
        new_elements.append(new_datum_element)

    # Create element values records
    for new_datum_element in new_elements:
        # Set element value table
        new_element_value_model = new_datum_element.element_type.element_data_type.element_value_class
        ElementValueModel = getattr(ElementValueModels, new_element_value_model)
        # Create element value
        new_element_value = ElementValueModel(element_type_datum_object=new_datum_element)
        new_element_value.save()

    return new_datum.datum_object_id