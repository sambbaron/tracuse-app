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

    fields = BaseModelAdmin.fields + ("user", "datum_type")
    readonly_fields = BaseModelAdmin.readonly_fields + ("element_types",)

    inlines = [ElementDatumObjectInline, ]


@admin.register(DatumType)
class DatumTypeAdmin(EntityModelAdmin):
    list_display = EntityModelAdmin.list_display + ("headline_expr", )
    list_editable = EntityModelAdmin.list_editable + ("headline_expr", )

    fields = EntityModelAdmin.fields + ("headline_expr", )

    inlines = [DatumObjectInline, ElementDatumTypeInline]


class DatumTypeInline(EntityModelInline):
    model = DatumType
    fields = EntityModelAdmin.fields + ("headline_expr", )


@admin.register(DatumGroup)
class DatumGroupAdmin(EntityModelAdmin):
    inlines = [DatumTypeInline, ]