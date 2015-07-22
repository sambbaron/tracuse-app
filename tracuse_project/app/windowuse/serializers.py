from app.utils.serializer import Serializer
from app.ui_object.serializers import UiObjectModelSerializer

from .models import WindowuseObject, WindowuseViewuse


class WindowuseObjectSerializer(UiObjectModelSerializer):
    model = WindowuseObject

    def serial_related(self):
        output = super().serial_default()
        output.append(("viewuse_objects", [viewuse.viewuse_object_id for viewuse in self.obj.windowuse_viewuses.all()]))
        return output

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
