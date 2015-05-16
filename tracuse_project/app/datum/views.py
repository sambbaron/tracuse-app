import json

from django.http import HttpResponse, JsonResponse, Http404
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder

from .models import DatumObject
from app.common.serializers import Serializer
from .serializers import DatumObjectSerializer


class DatumObjectAll(View):
    """
    List all datum_objects, or create a new datum_object.
    """
    # permission_classes = (IsAuthenticated, IsOwner,)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        super().dispatch(request, *args, **kwargs)
        # if obj.user == request.user

    def get(self, request):
        queryset = DatumObject.actives.all()
        serialized_data = Serializer(data=queryset,
                                     serializer=DatumObjectSerializer.serial_datum_all
                                     ).serialize()
        response_data = {"datum_object": serialized_data}
        response = JsonResponse(response_data, status=200)
        return response

    def post(self, request):
        serialized_data = json.loads(request.data, cls=DjangoJSONEncoder)
        post_data = post_datum_object(serialized_data)
        if type(post_data) == DatumObject:
            response = JsonResponse(post_data, status=201)
        else:
            response = HttpResponse(post_data, status=400)
        return response


class DatumObjectOne(View):
    """
    Retrieve, update or delete a datum_object instance.
    """

    @login_required
    def dispatch(self, request, *args, **kwargs):
        super().dispatch(request, *args, **kwargs)
        # if obj.user == request.user

    def get_object(self, pk):
        try:
            return DatumObject.objects.get(pk=pk)
        except DatumObject.DoesNotExist:
            raise Http404("Datum Object does not exist.")

    def get(self, request, pk):
        object = self.get_object(pk)
        serialized_data = Serializer(data=object,
                                     serializer=DatumObjectSerializer.serial_datum_all
                                     ).serialize()
        response = JsonResponse(serialized_data, status=200)
        return response

    def put(self, request, pk):
        serialized_data = json.loads(request.data, cls=DjangoJSONEncoder)
        post_data = post_datum_object(serialized_data)
        if type(post_data) == DatumObject:
            response = JsonResponse(post_data, status=200)
        else:
            response = HttpResponse(post_data, status=400)
        return response

    def delete(self, request, pk):
        datum_object = self.get_object(pk)
        datum_object.delete()
        return HttpResponse(status=204)