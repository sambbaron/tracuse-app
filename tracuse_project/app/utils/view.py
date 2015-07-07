from django.http import HttpResponse, Http404
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from app.utils.serializer import Serializer


class ViewBase(View):
    """Base View Class for all api-based views

    Attributes:
        model: Django model class
        serializer_class: Serializer class
        serializer_template/deserializer_template (string):
            template name - corresponds to serializer method
        serializer: Serializer instance with template for get calls
        deserializer: Serializer instance with template for put/post calls
            If not provided, same as 'serializer'
        queryset: Django queryset object
    """
    model = None
    queryset = None
    serializer_class = Serializer
    serializer_template = "serial_default"
    deserializer_template = None
    serializer_format = "json"
    deserializer_format = "json"

    def __init__(self, **kwargs):
        """Create serializer and deserializer instances """
        if self.serializer_class:
            self.serializer = self.serializer_class(self.serializer_template)

            if not self.deserializer_template:
                self.deserializer_template = self.serializer_template
            self.deserializer = self.serializer_class(self.deserializer_template)

        super().__init__(**kwargs)

    def serialized_data(self, data):
        serialized_data = self.serializer.serialize(data)
        encoded_data = self.serializer.encode(self.serializer_format, serialized_data)
        return encoded_data

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404("{} does not exist".format(self.model.__name__))

    def update_prep(self, request):
        """Pull  and decode request data
        Perform other prep tasks before updating model
        """
        request_data = request.body.decode()
        if self.deserializer_format == "form":
            return request.POST.dict()
        else:
            return self.deserializer.decode(self.deserializer_format, request_data)

    def update_model(self, model_object, model_update):
        """Save request data to model object using deserializer"""
        return self.deserializer.deserialize(model_object, model_update)

    def update_response(self, save_result, success_code, fail_code):
        """Return HTTP response for data update
        Assume that string response is an error
        """
        if type(save_result) == str:
            response = HttpResponse(save_result, status=fail_code)
        else:
            response_data = self.serialized_data(save_result)
            response = HttpResponse(response_data, status=success_code, content_type="application/json")

        return response


class ViewAll(ViewBase):
    """ Base View for all rows
    """

    http_method_names = ["get", "post"]

    def get(self, request):
        response_data = self.serialized_data(self.queryset)
        response = HttpResponse(response_data, status=200, content_type="application/json")
        return response

    def post(self, request):
        object = self.model()
        request_data = self.update_prep(request)
        save_result = self.update_model(object, request_data)
        response = self.update_response(save_result, 201, 400)
        return response


class ViewOne(ViewBase):
    """Base View for single object
    """

    http_method_names = ["get", "put", "delete"]

    def get(self, request, pk):
        object = self.get_object(pk)
        response_data = self.serialized_data(object)
        response = HttpResponse(response_data, status=200, content_type="application/json")
        return response

    def put(self, request, pk):
        object = self.get_object(pk)
        request_data = self.update_prep(request)
        save_result = self.update_model(object, request_data)
        response = self.update_response(save_result, 200, 400)
        return response

    def delete(self, request, pk):
        object = self.get_object(pk)
        object.delete()
        response = HttpResponse(status=204)
        return response


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
