from app.utils.view import ViewAll, ViewOne, LoginRequiredMixin

from .models import AssociationDirection, AssociationAll
from .serializers import AssociationDirectionSerializer, AssociationAllSerializer


class AssociationDirectionAll(LoginRequiredMixin, ViewAll):
    model = AssociationDirection
    queryset = AssociationDirection.objects.all()
    serializer_class = AssociationDirectionSerializer
