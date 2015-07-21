from django.db.models import Q

from app.utils.view import ViewAll, ViewOne, LoginRequiredMixin

from .models import ViewuseObject
from .serializers import ViewuseObjectSerializer


class ViewuseObjectAll(LoginRequiredMixin, ViewAll):
    model = ViewuseObject
    serializer_class = ViewuseObjectSerializer
    serializer_template = "serial_related"
    deserializer_template = "serial_update"

    @property
    def queryset(self):
        return ViewuseObject.actives.filter(Q(user=self.request.user) | Q(user=None)).all()


class ViewuseObjectOne(LoginRequiredMixin, ViewOne):
    model = ViewuseObject
    serializer_class = ViewuseObjectSerializer
    serializer_template = "serial_related"
    deserializer_template = "serial_update"
