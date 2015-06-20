"""Model Helper Functions"""

import json

from django.core.exceptions import FieldDoesNotExist


def convert_field_data(field_data, field_type):
    """ Convert model field data
    Use in deserialization of json data

    Attributes:
        field_data (any)
        field_type (string):
            Django field name or custom field name
    """
    output = field_data
    error_message = "err:'{}' data conversion failure".format(field_type)

    if field_type in ["BooleanField", "boolean"]:
        if field_data.lower() == "false":
            output = False
        else:
            output = bool(field_data)
    elif field_type in ["IntegerField", "BigIntegerField", "AutoField", "ForeignKey", "integer"]:
        try:
            output = int(field_data)
        except ValueError:
            return error_message
    elif field_type in ["json", ]:
        output = json.dumps(field_data)

    return output


def update_model(model_object, fields, data, request=None):
    """Helper function to update model data

        Attributes:
            model_object: model instance
            fields (list of tuples): Fields to update
                First: field name
                Second: data type or data source (ex: "request")
            data (dict): data to save
                Key: field name
                Value: value
            request: HTTP request object
                Used for session data - user, etc.

        Return:
            Saved model object or error message
    """

    for field in fields:

        field_name = field[0]

        try:
            model_field = model_object._meta.get_field(field_name)
        except FieldDoesNotExist:
            return "'{}' not a valid field".format(field_name)

        try:
            field_type = field[1]
        except IndexError:
            field_type = model_field.get_internal_type()

        # Set update data from HTTP request object
        if field_type == "request":
            request_data =  getattr(request, field_name)
            converted_data = request_data
        else:
            # Set update data from request data

            if field_name not in data:
                return "'{}' not in data request".format(field_name)

            request_data = data[field_name]
            converted_data = convert_field_data(request_data, field_type)

        if type(converted_data) == str and converted_data[:4] == "err:":
            return converted_data[4:] + "; Field: {}; Raw data: {};".format(field_name, request_data)

        try:
            setattr(model_object, field_name, converted_data)
        except:
            return "Error updating '{}'; Raw data: {}; Converted data: {};".format(field_name,
                                                                                  request_data,
                                                                                  converted_data
                                                                                  )

    model_object.save()

    return model_object
