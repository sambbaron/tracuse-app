import importlib

from django.apps import apps
from django.db.models import QuerySet


class Serializer(object):
    """Serialize object using classes/methods in app/serializers.py

    Attributes:
        data: Data to be serialized
        serializer:
            Serializer object: class.method object OR
            Serializer string: 'app_name.serializer_class.serializer.method'
        many: Whether data is single instance or multiple instances

    """

    def __init__(self, data, serializer):
        self.data = data
        self.serializer = serializer
        self.many = False


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
                serialized_obj = serializer(obj)
                output.append(serialized_obj)
        else:
            output = serializer(self.data)

        return output