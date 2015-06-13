from django.contrib import admin

from app.common.admin import EntityModelAdmin, EntityModelInline
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
class ViewuseObjectAdmin(EntityModelAdmin):
    list_display = EntityModelAdmin.list_display + ("viewuse_arrangement", "viewuse_datum", "filter_json", "filter_set",)
    list_editable = EntityModelAdmin.list_editable + ("viewuse_arrangement", "viewuse_datum", "filter_json", "filter_set",)

    fields = EntityModelAdmin.fields + ("viewuse_arrangement", "viewuse_datum", "filter_json", "filter_set",)