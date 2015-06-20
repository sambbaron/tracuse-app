from utils.view import ViewAll, ViewOne

from .models import DatumGroup, DatumType, DatumObject
from .serializers import (DatumGroupSerializer,
                          DatumTypeSerializer,
                          DatumObjectSerializer)


class DatumGroupAll(ViewAll):
    model = DatumGroup
    queryset = DatumGroup.actives.all()
    serializer = DatumGroupSerializer.serial_related


class DatumTypeAll(ViewAll):
    model = DatumType
    queryset = DatumType.actives.all()
    serializer = DatumTypeSerializer.serial_related


class DatumObjectAll(ViewAll):
    model = DatumObject
    serializer = DatumObjectSerializer.serial_related

    update_fields = [
        ("user", "request"),
        ("datum_type_id",)
    ]

    @property
    def queryset(self):
        return DatumObject.actives.filter(user=self.request.user).all()


class DatumObjectOne(ViewOne):
    model = DatumObject
    serializer = DatumObjectSerializer.serial_elements_object
