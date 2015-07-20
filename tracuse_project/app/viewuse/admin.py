from django.contrib import admin

from app.common.admin import BaseModelAdmin, BaseModelInline, EntityModelAdmin, EntityModelInline
from .models import ViewuseObject, ViewuseArrangement, ViewuseDatum, ViewuseNested


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


class ViewuseNestedInline(BaseModelInline):
    model = ViewuseNested

    fields = BaseModelInline.fields + ("nested_viewuse", "order", "height", "width",)
    fk_name = "parent_viewuse"


@admin.register(ViewuseNested)
class ViewuseNestedAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + ("parent_viewuse", "nested_viewuse", "order", "height", "width",)
    list_editable = BaseModelAdmin.list_editable + ("parent_viewuse", "nested_viewuse", "order", "height", "width",)

    fields = BaseModelAdmin.fields + ("parent_viewuse", "nested_viewuse", "order", "height", "width",)


class ViewuseObjectInline(EntityModelInline):
    model = ViewuseObject

    fields = EntityModelInline.fields + ("title", "description", "viewuse_arrangement", "viewuse_datum", "datum_filter",)


@admin.register(ViewuseObject)
class ViewuseObjectAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + ("title", "description", "viewuse_arrangement", "viewuse_datum", "datum_filter",)
    list_editable = BaseModelAdmin.list_editable + ("title", "description", "viewuse_arrangement", "viewuse_datum", "datum_filter",)

    fields = BaseModelAdmin.fields + ("title", "description", "viewuse_arrangement", "viewuse_datum", "datum_filter")

    inlines = [ViewuseNestedInline, ]
