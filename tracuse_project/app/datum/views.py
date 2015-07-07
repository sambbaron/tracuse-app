from utils.view import ViewAll, ViewOne, LoginRequiredMixin

from .models import DatumGroup, DatumType, DatumObject
from .serializers import (DatumGroupSerializer,
                          DatumTypeSerializer,
                          DatumObjectSerializer)


class DatumGroupAll(LoginRequiredMixin, ViewAll):
    model = DatumGroup
    queryset = DatumGroup.actives.all()
    serializer_class = DatumGroupSerializer
    serializer_template = "serial_related"


class DatumTypeAll(LoginRequiredMixin, ViewAll):
    model = DatumType
    queryset = DatumType.actives.all()
    serializer_class = DatumTypeSerializer
    serializer_template = "serial_related"


class DatumObjectAll(LoginRequiredMixin, ViewAll):
    model = DatumObject
    serializer_class = DatumObjectSerializer
    serializer_template = "serial_related"
    deserializer_template = "serial_post"

    @property
    def queryset(self):
        return DatumObject.actives.filter(user=self.request.user).all()

    def update_model(self, model_object, model_update):
        model_update["user"] = self.request.user
        return self.deserializer.deserialize(model_object, model_update)


class DatumObjectOne(LoginRequiredMixin, ViewOne):
    model = DatumObject
    serializer_class = DatumObjectSerializer
    serializer_template = "serial_elements_object"
