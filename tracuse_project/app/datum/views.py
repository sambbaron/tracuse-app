from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from app.common.permissions import IsOwner

from .models import DatumObject
from .serializers_rest import DatumObjectMainSerializer


class DatumObjectList(APIView):
    """
    List all datum_objects, or create a new datum_object.
    """
    permission_classes = (IsAuthenticated, IsOwner,)

    def get(self, request, format=None):
        datum_objects = DatumObject.actives.all()
        serializer = DatumObjectMainSerializer(datum_objects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DatumObjectMainSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DatumObjectDetail(APIView):
    """
    Retrieve, update or delete a datum_object instance.
    """
    permission_classes = (IsAuthenticated, IsOwner,)

    def get_object(self, pk):
        try:
            return DatumObject.objects.get(pk=pk)
        except DatumObject.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        datum_object = self.get_object(pk)
        serializer = DatumObjectMainSerializer(datum_object)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        datum_object = self.get_object(pk)
        serializer = DatumObjectMainSerializer(datum_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        datum_object = self.get_object(pk)
        datum_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)