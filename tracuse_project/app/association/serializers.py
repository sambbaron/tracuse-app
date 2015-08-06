from .models import AssociationDirection, AssociationAll

from app.utils.serializer import Serializer


class AssociationDirectionSerializer(Serializer):
    model = AssociationDirection


class AssociationAllSerializer(Serializer):
    model = AssociationAll

    def serial_parent(self):
        return [
            ("datum_object", self.obj.parent_datum_id),
            ("datum_object_id", self.obj.parent_datum_id),
            "distance"
        ]

    def serial_child(self):
        return [
            ("datum_object", self.obj.child_datum_id),
            ("datum_object_id", self.obj.child_datum_id),
            "distance"
        ]