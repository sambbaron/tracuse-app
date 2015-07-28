from django.contrib import admin

from app.common.admin import BaseModelAdmin, BaseModelInline, UiObjectModelAdmin, UiObjectModelInline
from .models import WindowuseObject, WindowuseViewuse


class WindowuseViewuseInline(BaseModelInline):
    model = WindowuseViewuse

    fields = BaseModelInline.fields + ("windowuse_object", "viewuse_object",)


@admin.register(WindowuseViewuse)
class WindowuseViewuseAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + ("windowuse_object", "viewuse_object",)
    list_editable = BaseModelAdmin.list_editable + ("windowuse_object", "viewuse_object",)

    fields = BaseModelAdmin.fields + ("windowuse_object", "viewuse_object",)


@admin.register(WindowuseObject)
class WindowuseObjectAdmin(UiObjectModelAdmin):
    list_display = UiObjectModelAdmin.list_display
    list_editable = UiObjectModelAdmin.list_editable

    fields = UiObjectModelAdmin.fields

    inlines = [WindowuseViewuseInline, ]
