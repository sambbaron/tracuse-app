from app.utils.serializer import Serializer
from app.common.serializers import UiObjectModelSerializer

from .models import ViewuseObject, ViewuseArrangement


class ViewuseObjectSerializer(UiObjectModelSerializer):
    model = ViewuseObject

    def serial_related(self):
        output = self.serial_default()
        output.append(("viewuse_arrangement", self.obj.viewuse_arrangement_id))
        return output

    def serial_update(self):
        output = super().serial_update()
        output.append("viewuse_arrangement_id")
        return output


class ViewuseArrangementSerializer(Serializer):
    model = ViewuseArrangement
