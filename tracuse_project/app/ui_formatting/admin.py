from django.contrib import admin

from app.common.admin import BaseModelAdmin, BaseModelInline, EntityModelAdmin, EntityModelInline
from .models import UiFormattingType, UiFormattingGeneric


class UiFormattingTypeInline(EntityModelInline):
    model = UiFormattingType


@admin.register(UiFormattingType)
class UiFormattingTypeAdmin(EntityModelAdmin):
    list_display = EntityModelAdmin.list_display
    list_editable = EntityModelAdmin.list_editable

    fields = EntityModelAdmin.fields
    readonly_fields = EntityModelAdmin.readonly_fields


class UiFormattingGenericInline(BaseModelInline):
    model = UiFormattingGeneric

    fields = BaseModelAdmin.fields


@admin.register(UiFormattingGeneric)
class UiFormattingGenericAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display
    list_editable = BaseModelAdmin.list_editable

    fields = BaseModelAdmin.fields
