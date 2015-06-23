from django.http import HttpResponse, Http404
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class ViewBase(View):
    """Base View Class for all api-based views

    Attributes:
        model: Django model class
        serializer: Serializer with template for get calls
        deserializer: Serializer with template for put/post calls
            If not provided, same as 'serializer'
        queryset: Django queryset object
    """
    model = None
    queryset = None
    serializer = None
    deserializer = None

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.serializer
        self.deserializer = self.deserializer or self.serializer
        return super().dispatch(request, *args, **kwargs)

    def serialized_data(self, data):
        self.serializer.data = data
        serialized_data = self.serializer.serialize()
        encoded_data = self.serializer.encode("json", serialized_data)
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
        return self.deserializer.decode("json", request_data)

    def update_model(self, model_object, model_update):
        """Save request data to model object using deserializer"""
        self.deserializer.data = model_object
        return self.deserializer.deserialize(model_update, self.request)

    def update_response(self, save_result, success_code, fail_code):
        """Return HTTP response for data update
        Assume that string response is an error
        """
        if type(save_result) == str:
            response = HttpResponse(save_result, status=fail_code)
        else:
            response_data = self.serialized_data(save_result)
            response = HttpResponse(response_data, status=success_code)

        return response


class ViewAll(ViewBase):
    """ Base View for all rows
    """

    def get(self, request):
        response_data = self.serialized_data(self.queryset)
        response = HttpResponse(response_data, status=200)
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

    def get(self, request, pk):
        object = self.get_object(pk)
        response_data = self.serialized_data(object)
        response = HttpResponse(response_data, status=200)
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
