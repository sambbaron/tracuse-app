from app.utils.view import ViewAll, ViewOne, LoginRequiredMixin

from .models import DatumGroup, DatumType, DatumObject
from .serializers import (DatumGroupSerializer,
                          DatumTypeSerializer,
                          DatumObjectSerializer)


class DatumGroupAll(LoginRequiredMixin, ViewAll):
    model = DatumGroup
    queryset = DatumGroup.actives.all()
    serializer_class = DatumGroupSerializer
    get_template = "serial_related"


class DatumTypeAll(LoginRequiredMixin, ViewAll):
    model = DatumType
    queryset = DatumType.actives.all()
    serializer_class = DatumTypeSerializer
    get_template = "serial_related"


class DatumObjectAll(LoginRequiredMixin, ViewAll):
    model = DatumObject
    serializer_class = DatumObjectSerializer
    get_template = "serial_related"
    post_template = "serial_post"
    response_template = "serial_related_object"

    @property
    def queryset(self):
        return DatumObject.actives.filter(user=self.request.user).all()

    def update_model(self, model_object, model_update):
        model_update["user"] = self.request.user
        return self.deserializer.deserialize(model_object, model_update)


class DatumObjectOne(LoginRequiredMixin, ViewOne):
    model = DatumObject
    serializer_class = DatumObjectSerializer
    get_template = "serial_related_object"
