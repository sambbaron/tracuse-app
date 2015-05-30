from django.contrib import admin

from app.common.admin import BaseModelAdmin, BaseModelInline, EntityModelAdmin, EntityModelInline
from .models import ViewuseObject, ViewuseArrangement, ViewuseDatum, ViewuseFilter


class ViewuseFilterInline(BaseModelInline):
    model = ViewuseFilter

    fields = BaseModelInline.fields + ("viewuse_object", "filter_json", "filter_set",)


@admin.register(ViewuseFilter)
class ViewuseFilterAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + ("viewuse_object", "filter_json", "filter_set",)
    list_editable = BaseModelAdmin.list_editable + ("viewuse_object", "filter_json", "filter_set",)

    fields = BaseModelAdmin.fields + ("viewuse_object", "filter_json", "filter_set",)


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
    list_display = EntityModelAdmin.list_display + ("viewuse_arrangement", "viewuse_datum",)
    list_editable = EntityModelAdmin.list_editable + ("viewuse_arrangement", "viewuse_datum",)

    fields = EntityModelAdmin.fields + ("viewuse_arrangement", "viewuse_datum",)

    inlines = [ViewuseFilterInline, ]
