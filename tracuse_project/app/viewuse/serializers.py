import json

from .models import (ViewuseObject,
                     ViewuseArrangement,
                     ViewuseDatum,
                     ViewuseNested)
from app.utils.serializer import Serializer


class ViewuseObjectSerializer(Serializer):
    model = ViewuseObject

    def serial_default(self):
        output = super().serial_default()
        output.remove("viewuse_filter")
        output.append(("viewuse_filter", json.loads(self.obj.viewuse_filter)))
        return output

    def serial_related(self):
        output = self.serial_default()
        output.append(("viewuse_arrangement", self.obj.viewuse_arrangement_id))
        output.append(("viewuse_datum", self.obj.viewuse_datum_id))
        output.append(("viewuse_nested", [viewuse_nested.viewuse_nested_id for viewuse_nested in self.obj.nested_viewuses.all()]))
        return output

    def serial_update(self):
        return [
            "title",
            "viewuse_arrangement_id",
            "viewuse_datum_id",
            ("viewuse_filter", json.dumps(self.obj.viewuse_filter))
        ]


class ViewuseArrangementSerializer(Serializer):
    model = ViewuseArrangement


class ViewuseDatumSerializer(Serializer):
    model = ViewuseDatum

class ViewuseNestedSerializer(Serializer):
    model = ViewuseNested

    def serial_related(self):
        output =  self.serial_default()
        output.append(("nested_title", self.obj.nested_viewuse.title))
        return output
