from django.contrib import admin

from app.common.admin import BaseModelAdmin, BaseModelInline, EntityModelAdmin, EntityModelInline
from .models import DatumGroup, DatumType, DatumObject
from app.element_type.admin import ElementDatumObjectInline, ElementDatumTypeInline


class DatumObjectInline(BaseModelInline):
    model = DatumObject


@admin.register(DatumObject)
class DatumObjectAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + ("user", "datum_type", "datum_group")
    list_editable = BaseModelAdmin.list_editable + ("user", "datum_type")

    fields = BaseModelAdmin.fields + ("datum_object_id", "user", "datum_type")
    readonly_fields = BaseModelAdmin.readonly_fields + ("datum_object_id", "element_types",)

    inlines = [ElementDatumObjectInline, ]


@admin.register(DatumType)
class DatumTypeAdmin(EntityModelAdmin):
    list_display = EntityModelAdmin.list_display + ("title_expression", "icon_class",)
    list_editable = EntityModelAdmin.list_editable + ("title_expression", "icon_class",)

    fields = EntityModelAdmin.fields + ("title_expression", "icon_class",)

    inlines = [ElementDatumTypeInline, ]


class DatumTypeInline(EntityModelInline):
    model = DatumType
    fields = EntityModelAdmin.fields + ("title_expression", )


@admin.register(DatumGroup)
class DatumGroupAdmin(EntityModelAdmin):
    inlines = [DatumTypeInline, ]