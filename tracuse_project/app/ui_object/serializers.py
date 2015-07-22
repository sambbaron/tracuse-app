import json

from .models import UiObjectModel, UiArrangementType, UiFormattingType
from app.utils.serializer import Serializer


class UiObjectModelSerializer(Serializer):
    model = UiObjectModel

    def serial_default(self):
        output = super().serial_default()
        output.remove("datum_filter")
        output.append(("datum_filter", json.loads(self.obj.datum_filter)))
        return output

    def serial_related(self):
        output = self.serial_default()
        output.append(("ui_arrangement_type", self.obj.ui_arrangement_type_id))
        output.append(("ui_formatting_type", self.obj.ui_formatting_type_id))
        return output

    def serial_update(self):
        return [
            "title",
            "description",
            "ui_arrangement_type_id",
            "ui_formatting_type_id",
            ("datum_filter", json.dumps(self.obj.datum_filter))
        ]


class UiArrangementTypeSerializer(Serializer):
    model = UiArrangementType


class UiFormattingTypeSerializer(Serializer):
    model = UiFormattingType
