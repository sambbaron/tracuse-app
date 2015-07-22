from app.utils.view import ViewAll, ViewOne, LoginRequiredMixin

from .models import UiArrangementType, UiFormattingType
from .serializers import UiArrangementTypeSerializer, UiFormattingTypeSerializer


class UiArrangementTypeAll(LoginRequiredMixin, ViewAll):
    model = UiArrangementType
    serializer_class = UiArrangementTypeSerializer


class UiFormattingTypeAll(LoginRequiredMixin, ViewAll):
    model = UiFormattingType
    serializer_class = UiFormattingTypeSerializer
