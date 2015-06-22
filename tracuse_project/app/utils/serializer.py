import json

from django.db.models import QuerySet
from django.core.serializers.json import DjangoJSONEncoder


class Serializer(object):
    """ Serialize and deserialize Django model data
    To/from JSON

    Attributes:
        model: Django model class
        data: Django model object or queryset
        template (string):
            Method name starting with "serial"
            Results in serialized object
        format (string): Convert into other format, like json
        object_wrap_pk (boolean):
            True:
                Wrap serialized data in dictionary
                with primary key as key
            False:
                Serialized data in list

    'Serialize' method outputs serialized object
    """
    model = None
    field_format = []

    def __init__(self, data=None, template=None, format=None, object_wrap_pk=False):
        self.data = data
        self.template = template or "serial_default"
        self.format = format
        self.object_wrap_pk = object_wrap_pk

    @property
    def _template_method(self):
        return getattr(self, self.template)

    def serial_default(self):
        """ All fields in model

        Use db columns, not django fields
        """
        output = {}
        for field in self.model._meta.fields:
            column_name = field.get_attname_column()[1]
            output[column_name] = getattr(self.obj, column_name)

        return output

    def _encode(self, data):
        """Format serialized data from python object"""

        output = data

        if self.format == "json":
            output = json.dumps(data,
                                cls=DjangoJSONEncoder,
                                indent=4
                                )

        return output

    def _decode(self, data):
        """Format serialized data from python object"""

        output = data

        if self.format == "json":
            output = json.loads(data,
                                cls=DjangoJSONEncoder,
                                indent=4
                                )

        return output

    def serialize(self):
        """ Serialize data from model object

        Use template method on model object
        Serializes QuerySets and individual object instances

        Return:
            Python object or encoded output
        """
        if not self.data:
            raise ValueError("Serializer has empty 'data' attribute")

        # Set output type
        if self.object_wrap_pk:
            output = {}
        else:
            output = []

        # Serialize Django queryset object
        if type(self.data) == QuerySet:

            for obj in self.data:
                self.obj = obj
                serialized_obj = self._template_method()

                if self.object_wrap_pk:
                    output[obj.pk] = serialized_obj
                else:
                    output.append(serialized_obj)

        # Serialize single object
        else:
            self.obj = self.data
            serialized_obj = self._template_method()
            if self.object_wrap_pk:
                output[self.obj.pk] = serialized_obj
            else:
                output = serialized_obj

        output = self._encode(output)

        return output
