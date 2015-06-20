import importlib
import json

from django.apps import apps
from django.db.models import QuerySet
from django.core.serializers.json import DjangoJSONEncoder


def serialize_all(model, instance):
    """Serialize all fields in model

    Use db columns, not django fields

    Attributes:
        model (django model)
        instance (model instance)

    Returns:
        Dictionary
            Key: column name
            Value: column value
    """
    output = {}
    for field in model._meta.fields:
        column_name = field.get_attname_column()[1]
        output[column_name] = getattr(instance, column_name)

    return output


class Serializer(object):
    """Serialize object using classes/methods in app/serializers.py

    Attributes:
        data: Data to be serialized
        serializer:
            Serializer object: class.method object OR
            Serializer string: 'app_name.serializer_class.serializer.method'
        format (string): Serialize output format
            If none, return dictionary
        dict_with_pk (boolean):
            True:
                Wrap serialized data in dictionary
                with primary key as dictionary key
            False:
                Serialized data in list
    """

    def __init__(self, data, serializer, dict_with_pk=False, format=None):
        self.data = data
        self.serializer = serializer
        self.format = format
        self.dict_with_pk = dict_with_pk

    def _set_serializer_method(self):
        """Convert serializer string to serializer method

        Assumes serializer class is in "serializers.py"
        String format: 'app_name.serializer_class.serializer.method'
        """

        serializer_method = self.serializer

        if isinstance(self.serializer, str):
            serializer_split = self.serializer.split(".")
            app_name_str = serializer_split[0]
            serializer_class_str = serializer_split[1]
            serializer_method_str = serializer_split[2]

            # Use Django app registry to retrieve app path
            app_path = apps.get_app_config(app_name_str).name

            serializer_module = importlib.import_module(app_path + ".serializers")
            serializer_class = getattr(serializer_module, serializer_class_str)
            serializer_method = getattr(serializer_class, serializer_method_str)

        return serializer_method

    def _format_output(self, dict_output):
        """Format serialized data into common type"""

        formatted_output = dict_output

        if self.format == "json":
            formatted_output = json.dumps(dict_output,
                                          cls=DjangoJSONEncoder,
                                          indent=4
                                          )

        return formatted_output

    def serialize(self):
        """Output serialized data using app serializers

        Serializes QuerySets and individual object instances
        """

        # Set serializer object
        serializer = self._set_serializer_method()

        # Set output type
        if self.dict_with_pk:
            output = {}
        else:
            output = []

        if type(self.data) == QuerySet:

            for obj in self.data:
                serialized_obj = serializer(obj)

                if self.dict_with_pk:
                    output[obj.pk] = serialized_obj
                else:
                    output.append(serialized_obj)

        else:
            serialized_obj = serializer(self.data)
            if self.dict_with_pk:
                output[self.data.pk] = serialized_obj
            else:
                output = serialized_obj

        output = self._format_output(output)

        return output
