from .models import AssociationDirection, AssociationAdjacent, AssociationAll

from app.utils.serializer import Serializer


class AssociationDirectionSerializer(Serializer):
    model = AssociationDirection


class AssociationAdjacentSerializer(Serializer):
    model = AssociationAdjacent

    def serial_related(self):
        output = self.serial_default()
        output.append(("parent_datum", self.obj.parent_datum_id))
        output.append(("child_datum", self.obj.child_datum_id))
        return output


class AssociationAllSerializer(Serializer):
    model = AssociationAll

    def serial_related(self):
        output = self.serial_default()
        output.append(("parent_datum", self.obj.parent_datum_id))
        output.append(("child_datum", self.obj.child_datum_id))
        return output
