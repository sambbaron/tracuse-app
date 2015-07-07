from .models import TracuserLanding

from app.utils.serializer import Serializer


class TracuserLandingSerializer(Serializer):
    model = TracuserLanding

    def serial_update(self):
        return [
            "name",
            "email",
            "comments"
        ]
