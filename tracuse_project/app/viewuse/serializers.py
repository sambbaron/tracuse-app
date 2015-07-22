from .models import ViewuseObject
from app.ui_object.serializers import UiObjectModelSerializer


class ViewuseObjectSerializer(UiObjectModelSerializer):
    model = ViewuseObject
