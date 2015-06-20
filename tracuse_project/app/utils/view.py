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
    queryset = None
    serializer = None

    @property
    def model(self):
        return self.queryset.model

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404("{} does not exist".format(self.model.__name__))

    def serialized_data(self, data):
        return Serializer(data=data,
                          serializer=self.serializer
                          ).serialize()


class ViewAll(ViewBase):
    """ Base View for all rows
    """

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

    def get(self, request, pk):
        object = self.get_object(pk)
        response_data = self.serialized_data(object)
        response = JsonResponse(response_data, status=200)
        return response

    def post(self, request, pk):
        object = self.model.objects.create()
        request_data = request.body.decode()
        serialized_data = json.loads(request_data, encoding=DjangoJSONEncoder)

        model_save = update_model(object, self.post_field_list, serialized_data)
        if type(model_save) == str:
            response = JsonResponse(model_save, status=400, safe=False)
        else:
            response_data = self.serialized_data(model_save)
            response = JsonResponse(response_data, status=201)

        return response

    def put(self, request, pk):
        object = self.get_object(pk)
        request_data = request.body.decode()
        serialized_data = json.loads(request_data, encoding=DjangoJSONEncoder)

        model_save = update_model(object, self.put_field_list, serialized_data)
        if type(model_save) == str:
            response = JsonResponse(model_save, status=400, safe=False)
        else:
            response_data = self.serialized_data(model_save)
            response = JsonResponse(response_data, status=200)

        return response

    def delete(self, request, pk):
        object = self.get_object(pk)
        object.delete()
        response = HttpResponse(status=204)
        return response
