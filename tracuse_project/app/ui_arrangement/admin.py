from django.contrib import admin

from app.common.admin import BaseModelAdmin, BaseModelInline, EntityModelAdmin, EntityModelInline
from .models import UiArrangementType, UiArrangementTile


class UiArrangementTypeInline(EntityModelInline):
    model = UiArrangementType


@admin.register(UiArrangementType)
class UiArrangementTypeAdmin(EntityModelAdmin):
    list_display = EntityModelAdmin.list_display
    list_editable = EntityModelAdmin.list_editable

    fields = EntityModelAdmin.fields
    readonly_fields = EntityModelAdmin.readonly_fields


class UiArrangementTileInline(BaseModelInline):
    model = UiArrangementTile

    fields = BaseModelAdmin.fields + ("direction", "wrap",)


@admin.register(UiArrangementTile)
class UiArrangementTileAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + ("direction", "wrap",)
    list_editable = BaseModelAdmin.list_editable + ("direction", "wrap",)

    fields = BaseModelAdmin.fields + ("direction", "wrap",)
