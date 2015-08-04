from django.utils.decorators import method_decorator

from app.utils.view import ViewAll, ViewOne

from .models import TracuserLanding
from .serializers import TracuserLandingSerializer


class TracuserLandingAll(ViewAll):
    model = TracuserLanding
    queryset = TracuserLanding.objects.all()
    serializer_class = TracuserLandingSerializer
    post_template = "serial_update"
    post_format = "form"
    http_method_names = ["post"]