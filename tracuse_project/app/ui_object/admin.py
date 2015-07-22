from django.contrib import admin

from app.common.admin import BaseModelAdmin, BaseModelInline, EntityModelAdmin, EntityModelInline

from .models import UiObjectModel, UiArrangementType, UiFormattingType


class UiObjectModelInline(BaseModelInline):
    model = UiObjectModel

    fields = BaseModelInline.fields + ("title", "description", "ui_arrangement_type", "ui_formatting_type", "datum_filter")


class UiObjectModelAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + ("title", "description", "ui_arrangement_type", "ui_formatting_type", "datum_filter",)
    list_editable = BaseModelAdmin.list_editable + ("title", "description", "ui_arrangement_type", "ui_formatting_type", "datum_filter",)

    fields = BaseModelAdmin.fields + ("title", "description", "ui_arrangement_type", "ui_formatting_type", "datum_filter")
    readonly_fields = BaseModelAdmin.readonly_fields


@admin.register(UiArrangementType)
class UiArrangementTypeAdmin(EntityModelAdmin):
    list_display = EntityModelAdmin.list_display
    list_editable = EntityModelAdmin.list_editable

    fields = EntityModelAdmin.fields


@admin.register(UiFormattingType)
class UiFormattingTypeAdmin(EntityModelAdmin):
    list_display = EntityModelAdmin.list_display
    list_editable = EntityModelAdmin.list_editable

    fields = EntityModelAdmin.fields
