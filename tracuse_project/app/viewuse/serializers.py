from app.utils.serializer import Serializer
from app.common.serializers import UiObjectModelSerializer

from .models import ViewuseObject, ViewuseArrangement


class ViewuseObjectSerializer(UiObjectModelSerializer):
    model = ViewuseObject

class ViewuseArrangementSerializer(Serializer):
    model = ViewuseArrangement
