from django.utils.decorators import method_decorator

from utils.view import ViewAll, ViewOne

from .models import TracuserLanding
from .serializers import TracuserLandingSerializer


class TracuserLandingAll(ViewAll):
    model = TracuserLanding
    queryset = TracuserLanding.objects.all()
    serializer_class = TracuserLandingSerializer
    deserializer_template = "serial_update"
    http_method_names = ["post"]

    def dispatch(self, request, *args, **kwargs):
        """Override dispatch to clear login_required"""
        self.request = request
        return super().dispatch(request, *args, **kwargs)
