"""
Custom flat JSON serializer schema
Dictionary of Lists of Dictionaries

key: model class name


"""

from __future__ import absolute_import, unicode_literals

import json
import sys
import warnings

from django.core.serializers.base import DeserializationError
from django.core.serializers.python import (
    Deserializer as PythonDeserializer, Serializer as PythonSerializer,
)
from django.core.serializers.json import DjangoJSONEncoder
from django.utils import six
from django.utils.encoding import force_text, is_protected_type
from django.utils.deprecation import RemovedInDjango19Warning


class Serializer(PythonSerializer):
    """
    Convert a queryset to JSON.
    """

    internal_use_only = False

    def _init_options(self):
        if json.__version__.split('.') >= ['2', '1', '3']:
            # Use JS strings to represent Python Decimal instances (ticket #16850)
            self.options.update({'use_decimal': False})
        self._current = None
        self.json_kwargs = self.options.copy()
        self.json_kwargs.pop('stream', None)
        self.json_kwargs.pop('fields', None)
        if self.options.get('indent'):
            # Prevent trailing spaces
            self.json_kwargs['separators'] = (',', ': ')

    # Copy full serialize method to capture queryset for model name
    def serialize(self, queryset, **options):
        """
        Serialize a queryset.
        """

        # Only change to superclass method
        self.queryset = queryset

        self.options = options

        self.stream = options.pop("stream", six.StringIO())
        self.selected_fields = options.pop("fields", None)
        self.use_natural_keys = options.pop("use_natural_keys", False)
        if self.use_natural_keys:
            warnings.warn("``use_natural_keys`` is deprecated; use ``use_natural_foreign_keys`` instead.",
                RemovedInDjango19Warning)
        self.use_natural_foreign_keys = options.pop('use_natural_foreign_keys', False) or self.use_natural_keys
        self.use_natural_primary_keys = options.pop('use_natural_primary_keys', False)

        self.start_serialization()
        self.first = True
        for obj in queryset:
            self.start_object(obj)
            # Use the concrete parent class' _meta instead of the object's _meta
            # This is to avoid local_fields problems for proxy models. Refs #17717.
            concrete_model = obj._meta.concrete_model
            for field in concrete_model._meta.local_fields:
                if field.serialize:
                    if field.rel is None:
                        if self.selected_fields is None or field.attname in self.selected_fields:
                            self.handle_field(obj, field)
                    else:
                        if self.selected_fields is None or field.attname[:-3] in self.selected_fields:
                            self.handle_fk_field(obj, field)
            for field in concrete_model._meta.many_to_many:
                if field.serialize:
                    if self.selected_fields is None or field.attname in self.selected_fields:
                        self.handle_m2m_field(obj, field)
            self.end_object(obj)
            if self.first:
                self.first = False
        self.end_serialization()
        return self.getvalue()

    def start_serialization(self):
        self._init_options()
        # Set class name as dictionary key
        class_name = force_text(self.queryset.model._meta.model_name)
        self.stream.write("{\"" + class_name + "\": [")

    def end_serialization(self):
        if self.options.get("indent"):
            self.stream.write("\n")
        self.stream.write("]}")
        if self.options.get("indent"):
            self.stream.write("\n")

    def end_object(self, obj):
        # self._current has the field data
        indent = self.options.get("indent")
        if not self.first:
            self.stream.write(",")
            if not indent:
                self.stream.write(" ")
        if indent:
            self.stream.write("\n")
        json.dump(self.get_dump_object(obj), self.stream,
                  cls=DjangoJSONEncoder, **self.json_kwargs)
        self._current = None

    def get_dump_object(self, obj):
        data = self._current
        if not self.use_natural_primary_keys or not hasattr(obj, 'natural_key'):
            data[obj._meta.pk.attname] = force_text(obj._get_pk_val(), strings_only=True)

        return data

    def getvalue(self):
        # Grand-parent super
        return super(PythonSerializer, self).getvalue()


def Deserializer(stream_or_string, **options):
    """
    Deserialize a stream or string of JSON data.
    """
    if not isinstance(stream_or_string, (bytes, six.string_types)):
        stream_or_string = stream_or_string.read()
    if isinstance(stream_or_string, bytes):
        stream_or_string = stream_or_string.decode('utf-8')
    try:
        objects = json.loads(stream_or_string)
        for obj in PythonDeserializer(objects, **options):
            yield obj
    except GeneratorExit:
        raise
    except Exception as e:
        # Map to deserializer error
        six.reraise(DeserializationError, DeserializationError(e), sys.exc_info()[2])