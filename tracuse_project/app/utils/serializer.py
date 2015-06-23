import json

from django.db.models import QuerySet
from django.core.serializers.json import DjangoJSONEncoder
from django.core.exceptions import FieldDoesNotExist


class Serializer(object):
    """ Serialize and deserialize Django model data
    To/from JSON

    Attributes:
        model: Django model class
        data: Django model object or queryset
        obj: Single object being serialized or deserialized
        template (string):
            Method name starting with "serial"
            Results in serialized object
        object_wrap_pk (boolean):
            True:
                Wrap serialized data in dictionary
                with primary key as key
            False:
                Serialized data in list

    Template property defines output structure
    List of Strings or Tuple
        First: field name
        Second: field value (if no field value, use field name)

    'Serialize' method outputs serialized object
    """
    model = None

    def __init__(self, data=None, template=None):
        self.data = data
        self.template = template or "serial_default"

    @property
    def _template(self):
        """Return template property from template string"""
        return getattr(self, self.template)

    @property
    def _template_fields(self):
        """Return field names from template as list of strings"""
        output = []
        for obj in self._template:
            if type(obj) == tuple:
                field_name = obj[0]
            else:
                field_name = obj
            output.append(field_name)

        return output

    @property
    def serial_default(self):
        """ All fields in model

        Use db columns, not django fields
        """
        output = []
        for field in self.model._meta.fields:
            output.append(field.get_attname_column()[1])

        return output

    @staticmethod
    def encode(format, data):
        """Format serialized data from python object"""

        output = data

        if format == "json":
            output = json.dumps(data, cls=DjangoJSONEncoder)

        return output

    @staticmethod
    def decode(format, data):
        """Format serialized data from python object"""

        output = data

        if format == "json":
            output = json.loads(data, encoding=DjangoJSONEncoder)

        return output

    def _serialize_template(self):
        """ Convert template into serialized object

        Return:
            Dictionary
                Key: field name
                Value: field value
        """
        output = {}
        for object in self._template:
            if type(object) == str:
                field_name = object
                field_value = None
            elif type(object) == tuple:
                field_name = object[0]
                field_value = object[1]
            else:
                raise AttributeError("Serial template object must be string or tuple")

            if field_value is None:
                try:
                    field_value = getattr(self.obj, field_name)
                except AttributeError:
                    raise AttributeError("'{}' not in object".format(field_name))

            output[field_name] = field_value

        return output

    def serialize(self, object_wrap_pk=False):
        """ Serialize data from model object

        Use template method on model object
        Serializes QuerySets and individual object instances

        Return:
            Python dictionary
        """
        if not self.data:
            raise ValueError("Serializer has empty 'data' attribute")

        # Set output type
        if object_wrap_pk:
            output = {}
        else:
            output = []

        # Serialize Django queryset object
        if type(self.data) == QuerySet:

            for obj in self.data:
                self.obj = obj
                serialized_obj = self._serialize_template()

                if object_wrap_pk:
                    output[obj.pk] = serialized_obj
                else:
                    output.append(serialized_obj)

        # Serialize single object
        elif type(self.data) == self.model:
            self.obj = self.data
            serialized_obj = self._serialize_template()
            if object_wrap_pk:
                output[self.obj.pk] = serialized_obj
            else:
                output = serialized_obj

        return output

    def deserialize(self, model_update, request):
        """Save data to model object using serializer template fields

        Attributes:
            model_update (object): Data to update object
            request: HTTP request object for session data

        Return:
            Saved model object
        """

        if self.data.__class__ == self.model:
            self.obj = self.data
        else:
            raise AttributeError("Object not instance of '{}'".format(self.model.__name__))

        fields = self._template_fields

        for field_name in fields:

            if field_name == "user":
                model_update["user"] = request.user

            try:
                self.obj._meta.get_field(field_name)
            except FieldDoesNotExist:
                return "'{}' not a valid field".format(field_name)

            if field_name not in model_update:
                return "'{}' not in data request".format(field_name)

            field_update = model_update[field_name]

            try:
                setattr(self.obj, field_name, field_update)
            except:
                return "Error updating '{}'; Update data: {};".format(field_name,
                                                                      model_update
                                                                      )

        self.obj.save()

        return self.obj
