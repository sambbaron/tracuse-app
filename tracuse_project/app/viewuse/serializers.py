from app.ui_object.serializers import UiObjectModelSerializer

from .models import ViewuseObject


class ViewuseObjectSerializer(UiObjectModelSerializer):
    model = ViewuseObject
