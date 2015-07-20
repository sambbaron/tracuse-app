from django.db.models import Q

from app.utils.view import ViewAll, ViewOne, LoginRequiredMixin

from .models import WindowuseObject, WindowuseViewuse
from .serializers import WindowuseObjectSerializer, WindowuseViewuseSerializer


class WindowuseObjectAll(LoginRequiredMixin, ViewAll):
    model = WindowuseObject
    serializer_class = WindowuseObjectSerializer
    serializer_template = "serial_default"
    deserializer_template = "serial_update"

    @property
    def queryset(self):
        return WindowuseObject.actives.filter(Q(user=self.request.user) | Q(user=None)).all()


class WindowuseObjectOne(LoginRequiredMixin, ViewOne):
    model = WindowuseObject
    serializer_class = WindowuseObjectSerializer
    serializer_template = "serial_default"
    deserializer_template = "serial_update"


class WindowuseViewuseAll(LoginRequiredMixin, ViewAll):
    model = WindowuseViewuse
    serializer_class = WindowuseViewuseSerializer
    serializer_template = "serial_related"

    @property
    def queryset(self):
        return WindowuseViewuse.actives. \
            filter(Q(windowuse_object__user=self.request.user) | Q(windowuse_object__user=None)).all()


class WindowuseViewuseOne(LoginRequiredMixin, ViewOne):
    model = WindowuseViewuse
    serializer_class = WindowuseViewuseSerializer
    serializer_template = "serial_related"
    deserializer_template = "serial_update"