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
        get_template/post_template (string):
            template name - corresponds to serializer method
        serializer: Serializer instance with template for get calls
        deserializer: Serializer instance with template for put/post calls
            If not provided, same as 'serializer'
        queryset: Django queryset object
    """
    model = None
    queryset = None
    serializer_class = Serializer
    get_template = "serial_default"
    post_template = None
    response_template = None
    get_format = "json"
    post_format = "json"

    def __init__(self, **kwargs):
        """ Set default serializer templates
            Create deserializer object
        """
        if self.serializer_class:

            if not self.post_template:
                self.post_template = self.get_template
            if not self.response_template:
                self.response_template = self.get_template

            self.deserializer = self.serializer_class(self.post_template)

        super().__init__(**kwargs)

    def serialized_data(self, data, template=None):
        if template is None:
            template = self.get_template
        serializer = self.serializer_class(template)
        serialized_data = serializer.serialize(data)
        encoded_data = serializer.encode(self.get_format, serialized_data)
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
        if self.post_format == "form":
            return request.POST.dict()
        else:
            return self.deserializer.decode(self.post_format, request_data)

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
            response_data = self.serialized_data(save_result, self.response_template)
            response = HttpResponse(response_data, status=success_code, content_type="application/json")

        return response


class ViewAll(ViewBase):
    """ Base View for all rows
    """

    http_method_names = ["get", "post"]

    def get(self, request, *args, **kwargs):
        response_data = self.serialized_data(self.queryset, self.get_template)
        response = HttpResponse(response_data, status=200, content_type="application/json")
        return response

    def post(self, request, *args, **kwargs):
        object = self.model()
        request_data = self.update_prep(request)
        save_result = self.update_model(object, request_data)
        response = self.update_response(save_result, 201, 400)
        return response


class ViewOne(ViewBase):
    """Base View for single object
    """

    http_method_names = ["get", "put", "delete"]

    def get(self, request, *args, **kwargs):
        object = self.get_object(kwargs["pk"])
        response_data = self.serialized_data(object, self.get_template)
        response = HttpResponse(response_data, status=200, content_type="application/json")
        return response

    def put(self, request, *args, **kwargs):
        object = self.get_object(kwargs["pk"])
        request_data = self.update_prep(request)
        save_result = self.update_model(object, request_data)
        response = self.update_response(save_result, 200, 400)
        return response

    def delete(self, request, *args, **kwargs):
        object = self.get_object(kwargs["pk"])
        object.delete()
        response = HttpResponse(status=204)
        return response


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
