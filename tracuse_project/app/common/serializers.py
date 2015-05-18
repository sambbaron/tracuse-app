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
        add_pk_key (boolean):
            Wrap serialized data in dictionary
            with primary key as dictionary key
    """

    def __init__(self, data, serializer, add_pk_key=False, format=None):
        self.data = data
        self.serializer = serializer
        self.format = format
        self.add_pk_key = add_pk_key

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

    def _add_pk_key(self, obj, output):
        """Add primary key to output"""
        new_output = output

        if self.add_pk_key:
            new_output = {obj.pk: output}

        return new_output

    def _serialize_one(self, obj, serializer):
        """Serialize one object instance and add primary key"""
        output = serializer(obj)
        if self.add_pk_key:
            output = self._add_pk_key(obj, output)
        return output

    def serialize(self):
        """Output serialized data using app serializers

        Returns:
            If QuerySet, list of serialized dictionaries
            If individual instance, serialized dictionary
        """
        serializer = self._set_serializer_method()

        if type(self.data) == QuerySet:
            output = []
            for obj in self.data:
                serialized_obj = self._serialize_one(obj, serializer)
                output.append(serialized_obj)
        else:
            output = self._serialize_one(self.data, serializer)

        output = self._format_output(output)

        return output
