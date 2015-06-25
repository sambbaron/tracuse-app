import json
import datetime
import decimal

from django.db.models import QuerySet
from django.core.serializers.json import DjangoJSONEncoder
from django.core.exceptions import FieldDoesNotExist


class Serializer(object):
    """ Serialize and deserialize Django model data
    To/from JSON

    Attributes:
        model: Django model class
        obj: Object being serialized or deserialized
        template (string):
            Method name starting with "serial"
            Results in serialized object

    Template method defines output structure using 'obj' property
        Returns List of Strings or Tuple
            First: field name
            Second: field value (if no field value, use field name)
    """
    model = None

    def __init__(self, template=None):
        self.template = template or "serial_default"

    def _template(self):
        """Return template property from template string"""
        return getattr(self, self.template)()

    def _template_fields(self):
        """Return field names from template as list of strings"""
        output = []
        for obj in self._template():
            if type(obj) == tuple:
                field_name = obj[0]
            else:
                field_name = obj
            output.append(field_name)

        return output

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
            output = json.dumps(data, cls=CustomJSONEncoder)
        return output

    @staticmethod
    def decode(format, data):
        """Format serialized data from python object"""
        output = data
        if format == "json":
            output = json.loads(data, parse_float=decimal.Decimal)
        return output

    def _serialize_template(self):
        """ Convert template into serialized object

        Return:
            Dictionary
                Key: field name
                Value: field value
        """
        output = {}
        for object in self._template():
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
                    return "'{}' not in data object".format(field_name)

            output[field_name] = field_value

        return output

    def serialize(self, model_object, object_wrap_pk=False):
        """ Serialize data from model object

        model_object: Model QuerySet or single object
        object_wrap_pk (boolean):
            True:
                Wrap serialized data in dictionary
                with primary key as key
            False:
                Serialized data in list

        Return:
            Python dictionary
        """

        # Set output type
        if object_wrap_pk:
            output = {}
        else:
            output = []

        # Serialize Django queryset object
        if type(model_object) == QuerySet:

            for object in model_object:
                self.obj = object
                serialized_obj = self._serialize_template()

                if object_wrap_pk:
                    output[self.obj.pk] = serialized_obj
                else:
                    output.append(serialized_obj)

        # Serialize single object
        elif type(model_object) == self.model:
            self.obj = model_object
            serialized_obj = self._serialize_template()

            if object_wrap_pk:
                output[self.obj.pk] = serialized_obj
            else:
                output = serialized_obj

        return output

    def deserialize(self, model_object, update_object):
        """Save data to model object using serializer template fields

        Attributes:
            model_object: Single model object
            update_object (dict): Data to update model
            request: HTTP request object for session data

        Return:
            Saved model object
        """

        if type(model_object) != self.model:
            raise AttributeError("Object not instance of '{}'".format(self.model.__name__))

        # Add update_object keys as attributes to 'obj' property
        self.obj = type('UpdateObject', (object,), update_object)

        # Convert update_object into serial template
        update_object = self._serialize_template()
        # Error if string
        if type(update_object) == str:
            return update_object

        # Update model object
        for field_name, field_value in update_object.items():

            try:
                self.model._meta.get_field(field_name)
            except FieldDoesNotExist:
                return "'{}' not a valid field".format(field_name)

            try:
                setattr(model_object, field_name, field_value)
            except:
                return "Error updating '{}'; Update value: {};".format(field_name,
                                                                       field_value
                                                                       )

        model_object.save()

        return model_object


class CustomJSONEncoder(json.JSONEncoder):
    """ JSONEncoder subclass that knows how to encode date/time and decimal types.

    Modeled after DjangoJSONEncoder, except convert decimal to float
    """
    def default(self, o):
        # See "Date Time String Format" in the ECMA-262 specification.
        if isinstance(o, datetime.datetime):
            r = o.isoformat()
            if o.microsecond:
                r = r[:23] + r[26:]
            if r.endswith('+00:00'):
                r = r[:-6] + 'Z'
            return r
        elif isinstance(o, datetime.date):
            return o.isoformat()
        elif isinstance(o, datetime.time):
            r = o.isoformat()
            if o.microsecond:
                r = r[:12]
            return r
        elif isinstance(o, decimal.Decimal):
            return o.__float__()
        else:
            return super().default(o)
