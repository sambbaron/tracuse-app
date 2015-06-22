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
    serializer = ViewuseObjectSerializer(template="serial_related")

    @property
    def queryset(self):
        return ViewuseObject.actives.filter(Q(user=self.request.user) | Q(user=None)).all()


class ViewuseObjectOne(ViewOne):
    model = ViewuseObject
    serializer = ViewuseObjectSerializer(template="serial_related")
    update_fields = [
        ("readable_name",),
        ("viewuse_arrangement_id",),
        ("viewuse_datum_id",),
        ("filter_json", "json"),
    ]


class ViewuseArrangementAll(ViewAll):
    model = ViewuseArrangement
    queryset = ViewuseArrangement.actives.all()
    serializer = ViewuseArrangementSerializer(template="serial_default")


class ViewuseDatumAll(ViewAll):
    model = ViewuseDatum
    queryset = ViewuseDatum.actives.all()
    serializer = ViewuseDatumSerializer(template="serial_default")
