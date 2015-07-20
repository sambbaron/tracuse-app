import json

from app.utils.serializer import Serializer

from .models import WindowuseObject, WindowuseViewuse


class WindowuseObjectSerializer(Serializer):
    model = WindowuseObject

    def serial_default(self):
        output = super().serial_default()
        output.remove("datum_filter")
        output.append(("datum_filter", json.loads(self.obj.datum_filter)))
        return output

    def serial_related(self):
        output = self.serial_default()
        output.append(("viewuse_objects", [viewuse.viewuse_object_id for viewuse in self.obj.windowuse_viewuses.all()]))
        return output

    def serial_update(self):
        return [
            "title",
            "description",
            ("datum_filter", json.dumps(self.obj.datum_filter))
        ]


class WindowuseViewuseSerializer(Serializer):
    model = WindowuseViewuse

    def serial_related(self):
        output = self.serial_default()
        output.append(("windowuse_object", self.obj.windowuse_object_id))
        output.append(("viewuse_object", self.obj.viewuse_object_id))
        return output

    def serial_update(self):
        return [
            "sort",
            "windowuse_object_id",
            "viewuse_object_id"
        ]
