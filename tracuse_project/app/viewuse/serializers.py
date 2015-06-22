import json

from .models import (ViewuseObject,
                     ViewuseArrangement,
                     ViewuseDatum)
from app.utils.serializer import Serializer


class ViewuseObjectSerializer(Serializer):
    model = ViewuseObject

    def serial_default(self):
        output = super().serial_default()
        output["filter_json"] = json.loads(output["filter_json"])
        return output

    def serial_related(self):
        output = self.serial_default()
        output["viewuse_arrangement"] = self.obj.viewuse_arrangement_id
        output["viewuse_datum"] = self.obj.viewuse_datum_id
        return output


class ViewuseArrangementSerializer(Serializer):
    model = ViewuseArrangement


class ViewuseDatumSerializer(Serializer):
    model = ViewuseDatum