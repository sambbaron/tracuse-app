import json

from django.http import HttpResponse, JsonResponse, Http404
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder

from utils.serializer import Serializer
from utils.model import update_model


class ViewBase(View):
    """Base View Class for all api-based views

    Attributes:
        queryset: Django queryset object
        serializer: Custom serializer class
    """
    model = None
    serializer = None

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404("{} does not exist".format(self.model.__name__))

    @classmethod
    def serialized_data(cls, data):
        return Serializer(data=data,
                          serializer=cls.serializer
                          ).serialize()


class ViewAll(ViewBase):
    """ Base View for all rows
    """
    queryset = None

    def get(self, request):
        response_data = self.serialized_data(self.queryset)
        response = JsonResponse(response_data, status=200, safe=False)
        return response


class ViewOne(ViewBase):
    """Base View for single object

    Attributes:
        field_list (string list):
            Field names for data update
        post_field_list (string list):
            Optional field list specifically for posts
        put_field_list (string list):
            Optional field list specifically for puts
    """
    field_list = []
    post_field_list = field_list
    put_field_list = field_list

    def update_prep(self, request):
        """Convert request data to python object"""
        request_data = request.body.decode()
        return json.loads(request_data, encoding=DjangoJSONEncoder)

    def update_save(self, model_object, request_data):
        """Save request data to model object"""
        return update_model(model_object, self.post_field_list, request_data)

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

    def get(self, request, pk):
        object = self.get_object(pk)
        response_data = self.serialized_data(object)
        response = JsonResponse(response_data, status=200)
        return response

    def post(self, request, pk):
        object = self.model.objects.create()
        request_data = self.update_prep(request)
        save_result = self.update_save(object, request_data)
        response = self.update_response(save_result, 201, 400)
        return response

    def put(self, request, pk):
        object = self.get_object(pk)
        request_data = self.update_prep(request)
        save_result = self.update_save(object, request_data)
        response = self.update_response(save_result, 200, 400)
        return response

    def delete(self, request, pk):
        object = self.get_object(pk)
        object.delete()
        response = HttpResponse(status=204)
        return response
