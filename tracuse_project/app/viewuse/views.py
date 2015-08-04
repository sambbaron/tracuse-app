from django.db.models import Q

from app.utils.view import ViewAll, ViewOne, LoginRequiredMixin

from .models import ViewuseObject, ViewuseArrangement
from .serializers import ViewuseObjectSerializer, ViewuseArrangementSerializer


class ViewuseObjectAll(LoginRequiredMixin, ViewAll):
    model = ViewuseObject
    serializer_class = ViewuseObjectSerializer
    get_template = "serial_related"
    post_template = "serial_update"

    @property
    def queryset(self):
        return ViewuseObject.actives.filter(Q(user=self.request.user) | Q(user=None)).all()


class ViewuseObjectOne(LoginRequiredMixin, ViewOne):
    model = ViewuseObject
    serializer_class = ViewuseObjectSerializer
    get_template = "serial_related"
    post_template = "serial_update"


class ViewuseArrangementAll(LoginRequiredMixin, ViewAll):
    model = ViewuseArrangement
    queryset = ViewuseArrangement.actives.all()
    serializer_class = ViewuseArrangementSerializer
