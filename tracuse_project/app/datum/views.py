from utils.view import ViewAll, ViewOne

from .models import DatumGroup, DatumType, DatumObject
from .serializers import (DatumGroupSerializer,
                          DatumTypeSerializer,
                          DatumObjectSerializer)


class DatumGroupAll(ViewAll):
    model = DatumGroup
    queryset = DatumGroup.actives.all()
    serializer = DatumGroupSerializer(template="serial_related")


class DatumTypeAll(ViewAll):
    model = DatumType
    queryset = DatumType.actives.all()
    serializer = DatumTypeSerializer(template="serial_related")


class DatumObjectAll(ViewAll):
    model = DatumObject
    serializer = DatumObjectSerializer(template="serial_related")

    @property
    def queryset(self):
        return DatumObject.actives.filter(user=self.request.user).all()


class DatumObjectOne(ViewOne):
    model = DatumObject
    serializer = DatumObjectSerializer(template="serial_elements_object")
