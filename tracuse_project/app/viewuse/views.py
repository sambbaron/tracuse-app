from django.db.models import Q

from app.utils.view import ViewAll, ViewOne, LoginRequiredMixin

from .models import (ViewuseObject,
                     ViewuseArrangement,
                     ViewuseDatum,
                     ViewuseNested)
from .serializers import (ViewuseObjectSerializer,
                          ViewuseArrangementSerializer,
                          ViewuseDatumSerializer,
                          ViewuseNestedSerializer)


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


class ViewuseArrangementAll(LoginRequiredMixin, ViewAll):
    model = ViewuseArrangement
    queryset = ViewuseArrangement.actives.all()
    serializer_class = ViewuseArrangementSerializer
    serializer_template = "serial_default"


class ViewuseDatumAll(LoginRequiredMixin, ViewAll):
    model = ViewuseDatum
    queryset = ViewuseDatum.actives.all()
    serializer_class = ViewuseDatumSerializer
    serializer_template = "serial_default"


class ViewuseNestedAll(LoginRequiredMixin, ViewAll):
    model = ViewuseNested
    queryset = ViewuseNested.actives.all()
    serializer_class = ViewuseNestedSerializer
    serializer_template = "serial_related"


class ViewuseNestedOne(LoginRequiredMixin, ViewOne):
    model = ViewuseNested
    serializer_class = ViewuseNestedSerializer