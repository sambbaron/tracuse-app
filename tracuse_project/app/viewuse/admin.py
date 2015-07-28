from django.contrib import admin

from app.common.admin import UiObjectModelAdmin, UiObjectModelInline, EntityModelAdmin, EntityModelInline
from .models import ViewuseObject, ViewuseArrangement


class ViewuseObjectInline(UiObjectModelInline):
    model = ViewuseObject

    fields = UiObjectModelInline.fields + ("viewuse_arrangement",)


@admin.register(ViewuseObject)
class ViewuseObjectAdmin(UiObjectModelAdmin):
    list_display = UiObjectModelAdmin.list_display + ("viewuse_arrangement",)
    list_editable = UiObjectModelAdmin.list_editable + ("viewuse_arrangement",)

    fields = UiObjectModelAdmin.fields + ("viewuse_arrangement",)


class ViewuseArrangementInline(EntityModelInline):
    model = ViewuseArrangement

    fields = EntityModelInline.fields


@admin.register(ViewuseArrangement)
class ViewuseArrangementAdmin(EntityModelAdmin):
    list_display = EntityModelAdmin.list_display
    list_editable = EntityModelAdmin.list_editable

    fields = EntityModelAdmin.fields
