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
