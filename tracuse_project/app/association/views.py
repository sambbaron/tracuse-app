from app.utils.view import ViewAll, ViewOne, LoginRequiredMixin

from .models import AssociationDirection
from .serializers import AssociationDirectionSerializer


class AssociationDirectionAll(LoginRequiredMixin, ViewAll):
    model = AssociationDirection
    queryset = AssociationDirection.objects.all()
    serializer_class = AssociationDirectionSerializer
