from django.db.models import Q

from utils.view import ViewAll, ViewOne

from .models import (ViewuseObject,
                     ViewuseArrangement,
                     ViewuseDatum)
from .serializers import (ViewuseObjectSerializer,
                          ViewuseArrangementSerializer,
                          ViewuseDatumSerializer)


class ViewuseObjectAll(ViewAll):
    model = ViewuseObject
    serializer = ViewuseObjectSerializer.serial_related

    @property
    def queryset(self):
        return ViewuseObject.actives.filter(Q(user=self.request.user) | Q(user=None)).all()


class ViewuseObjectOne(ViewOne):
    model = ViewuseObject
    serializer = ViewuseObjectSerializer.serial_related
    update_fields = [
        ("readable_name",),
        ("viewuse_arrangement_id",),
        ("viewuse_datum_id",),
        ("filter_json", "json"),
    ]


class ViewuseArrangementAll(ViewAll):
    model = ViewuseArrangement
    queryset = ViewuseArrangement.actives.all()
    serializer = ViewuseArrangementSerializer.serial_basic


class ViewuseDatumAll(ViewAll):
    model = ViewuseDatum
    queryset = ViewuseDatum.actives.all()
    serializer = ViewuseDatumSerializer.serial_basic
