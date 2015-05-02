"""****NOT WORKING
Custom flat JSON serializer schema
Dictionary of Lists of Dictionaries

key: model class name  ****UNABLE TO CATCH MODEL CHANGES IN SERIALIZATION
values: field/value dictionary
"""

from django.core.serializers.json import Serializer as JsonSerializer
from django.utils.encoding import force_text


class Serializer(JsonSerializer):
    """Extend built-in json serializer
    """

    def serialize(self, queryset, **options):
        # Set queryset argument as serializer property
        # to add model name to output
        self.queryset = queryset
        super().serialize(queryset, **options)

    def start_serialization(self):
        self._init_options()
        # Set class name as dictionary key
        # ****QUERYSET IS NOT ACTUAL QUERYSET OBJECT
        # ****GENERATOR OBJECT CONTAINING ALL OBJECTS
        # class_name = force_text(self.queryset.model._meta.model_name)
        class_name = "Test"
        self.stream.write("{\"" + class_name + "\": [")

    def end_serialization(self):
        if self.options.get("indent"):
            self.stream.write("\n")
        self.stream.write("]}")
        if self.options.get("indent"):
            self.stream.write("\n")

    def get_dump_object(self, obj):
        # Use flat field/value output
        data = self._current
        if not self.use_natural_primary_keys or not hasattr(obj, 'natural_key'):
            data[obj._meta.pk.attname] = force_text(obj._get_pk_val(), strings_only=True)
        return data