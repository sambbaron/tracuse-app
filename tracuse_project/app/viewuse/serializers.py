import json

from .models import (ViewuseObject,
                     ViewuseArrangement,
                     ViewuseDatum)
from app.utils.serializer import Serializer


class ViewuseObjectSerializer(Serializer):
    model = ViewuseObject

    def serial_default(self):
        output = super().serial_default()
        output.remove("filter_json")
        output.append(("filter_json", json.loads(self.obj.filter_json)))
        return output

    def serial_related(self):
        output = self.serial_default()
        output.append(("viewuse_arrangement", self.obj.viewuse_arrangement_id))
        output.append(("viewuse_datum", self.obj.viewuse_datum_id))
        return output

    def serial_update(self):
        return [
            "readable_name",
            "viewuse_arrangement_id",
            "viewuse_datum_id",
            "filter_json"
        ]


class ViewuseArrangementSerializer(Serializer):
    model = ViewuseArrangement


class ViewuseDatumSerializer(Serializer):
    model = ViewuseDatum
