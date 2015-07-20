from django.contrib import admin

from app.common.admin import BaseModelAdmin, BaseModelInline, EntityModelAdmin, EntityModelInline
from .models import WindowuseObject, WindowuseViewuse


@admin.register(WindowuseViewuse)
class WindowuseViewuseAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + ("windowuse_object", "viewuse_object",)
    list_editable = BaseModelAdmin.list_editable + ("windowuse_object", "viewuse_object",)

    fields = BaseModelAdmin.fields + ("windowuse_object", "viewuse_object",)


class WindowuseViewuseInline(BaseModelInline):
    model = WindowuseViewuse

    fields = BaseModelInline.fields + ("windowuse_object", "viewuse_object",)


@admin.register(WindowuseObject)
class WindowuseObjectAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + ("title", "description", "datum_filter",)
    list_editable = BaseModelAdmin.list_editable + ("title", "description", "datum_filter",)

    fields = BaseModelAdmin.fields + ("title", "description", "datum_filter")

    inlines = [WindowuseViewuseInline, ]
