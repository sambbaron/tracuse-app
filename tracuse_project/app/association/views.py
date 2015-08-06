from app.utils.view import ViewAll, ViewOne, LoginRequiredMixin

from .models import AssociationDirection, AssociationAll
from .serializers import AssociationDirectionSerializer, AssociationAllSerializer


class AssociationDirectionAll(LoginRequiredMixin, ViewAll):
    model = AssociationDirection
    queryset = AssociationDirection.objects.all()
    serializer_class = AssociationDirectionSerializer


class DatumAssociationParent(LoginRequiredMixin, ViewAll):
    model = AssociationAll
    serializer_class = AssociationAllSerializer
    get_template = "serial_parent"

    @property
    def queryset(self):
        return AssociationAll.objects.filter(child_datum_id=self.options["datum_pk"]).all()


class DatumAssociationChild(LoginRequiredMixin, ViewAll):
    model = AssociationAll
    serializer_class = AssociationAllSerializer
    get_template = "serial_child"

    @property
    def queryset(self):
        return AssociationAll.objects.filter(parent_datum_id=self.options["datum_pk"]).all()
