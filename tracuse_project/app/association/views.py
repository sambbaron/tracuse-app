from utils.view import ViewAll, ViewOne

from .models import AssociationDirection
from .serializers import AssociationDirectionSerializer


class AssociationDirectionAll(ViewAll):
    model = AssociationDirection
    queryset = AssociationDirection.objects.all()
    serializer_class = AssociationDirectionSerializer