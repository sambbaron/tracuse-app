from django.contrib import admin

from app.common.admin import BaseModelAdmin, BaseModelInline, EntityModelAdmin, EntityModelInline
from .models import ViewuseObject, ViewuseArrangement, ViewuseDatum


class ViewuseArrangementInline(EntityModelInline):
    model = ViewuseArrangement

    fields = EntityModelInline.fields


@admin.register(ViewuseArrangement)
class ViewuseArrangementAdmin(EntityModelAdmin):
    list_display = EntityModelAdmin.list_display
    list_editable = EntityModelAdmin.list_editable

    fields = EntityModelAdmin.fields


class ViewuseDatumInline(EntityModelInline):
    model = ViewuseDatum

    fields = EntityModelInline.fields


@admin.register(ViewuseDatum)
class ViewuseDatumAdmin(EntityModelAdmin):
    list_display = EntityModelAdmin.list_display
    list_editable = EntityModelAdmin.list_editable

    fields = EntityModelAdmin.fields


class ViewuseObjectInline(EntityModelInline):
    model = ViewuseObject

    fields = EntityModelInline.fields + ("viewuse_arrangement",)


@admin.register(ViewuseObject)
class ViewuseObjectAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + ("title", "description", "viewuse_arrangement", "viewuse_datum", "viewuse_filter",)
    list_editable = BaseModelAdmin.list_editable + ("title", "description", "viewuse_arrangement", "viewuse_datum", "viewuse_filter",)

    fields = BaseModelAdmin.fields + ("title", "description", "viewuse_arrangement", "viewuse_datum", "viewuse_filter",)
