import json

from app.utils.serializer import Serializer
from .models import UiObjectModel


class UiObjectModelSerializer(Serializer):
    model = UiObjectModel

    def serial_default(self):
        output = super().serial_default()
        output.remove("datum_filter")
        output.append(("datum_filter", json.loads(self.obj.datum_filter)))
        return output

    def serial_related(self):
        output = self.serial_default()
        return output

    def serial_update(self):
        return [
            "title",
            "description",
            ("datum_filter", json.dumps(self.obj.datum_filter))
        ]
