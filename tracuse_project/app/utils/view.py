import json

from django.http import HttpResponse, JsonResponse, Http404
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder

from utils.model import update_model


class ViewBase(View):
    """Base View Class for all api-based views

    Attributes:
        model: Django model class
        serializer: Custom serializer class
        queryset: Django queryset object
        update_fields (list of strings):
            Field names for data update
    """
    model = None
    serializer = None
    queryset = None
    update_fields = []

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @classmethod
    def serialized_data(cls, data):
        cls.serializer.data = data
        return cls.serializer.serialize()

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404("{} does not exist".format(self.model.__name__))

    def update_decode(self, request):
        """Convert request data to python object"""
        request_data = request.body.decode()
        return json.loads(request_data, encoding=DjangoJSONEncoder)

    def update_model(self, model_object, request_data, request_object):
        """Save request data to model object"""
        return update_model(model_object, self.update_fields, request_data, request_object)

    def update_response(self, save_result, success_code, fail_code):
        """Return HTTP response for data update
        Assume that string response is an error
        """
        if type(save_result) == str:
            response = JsonResponse(save_result, status=fail_code, safe=False)
        else:
            response_data = self.serialized_data(save_result)
            response = JsonResponse(response_data, status=success_code)

        return response


class ViewAll(ViewBase):
    """ Base View for all rows
    """

    def get(self, request):
        response_data = self.serialized_data(self.queryset)
        response = JsonResponse(response_data, status=200, safe=False)
        return response

    def post(self, request):
        object = self.model()
        request_data = self.update_decode(request)
        save_result = self.update_model(object, request_data, request)
        response = self.update_response(save_result, 201, 400)
        return response


class ViewOne(ViewBase):
    """Base View for single object
    """

    def get(self, request, pk):
        object = self.get_object(pk)
        response_data = self.serialized_data(object)
        response = JsonResponse(response_data, status=200)
        return response

    def put(self, request, pk):
        object = self.get_object(pk)
        request_data = self.update_decode(request)
        save_result = self.update_model(object, request_data, request)
        response = self.update_response(save_result, 200, 400)
        return response

    def delete(self, request, pk):
        object = self.get_object(pk)
        object.delete()
        response = HttpResponse(status=204)
        return response
