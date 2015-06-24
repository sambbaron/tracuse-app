from .models import AssociationDirection

from app.utils.serializer import Serializer


class AssociationDirectionSerializer(Serializer):
    model = AssociationDirection