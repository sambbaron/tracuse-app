from django.contrib import admin

from app.common.admin import BaseMixinAdmin, BaseMixinInline, EntityMixinAdmin, EntityMixinInline
from .models import DatumGroup, DatumType, DatumObject
from app.element_type.admin import ElementDatumObjectInline, ElementDatumTypeInline


class DatumObjectInline(BaseMixinInline):
    model = DatumObject


@admin.register(DatumObject)
class DatumObjectAdmin(BaseMixinAdmin):
    list_display = BaseMixinAdmin.list_display + ("user", "datum_type", "datum_group")
    list_editable = BaseMixinAdmin.list_editable + ("user", "datum_type")

    fields = BaseMixinAdmin.fields + ("user", "datum_type")
    readonly_fields = BaseMixinAdmin.readonly_fields + ("element_types",)

    inlines = [ElementDatumObjectInline, ]


@admin.register(DatumType)
class DatumTypeAdmin(EntityMixinAdmin):
    list_display = EntityMixinAdmin.list_display + ("repr_expression", )
    list_editable = EntityMixinAdmin.list_editable + ("repr_expression", )

    fields = EntityMixinAdmin.fields + ("repr_expression", )

    inlines = [DatumObjectInline, ElementDatumTypeInline]


class DatumTypeInline(EntityMixinInline):
    model = DatumType
    fields = EntityMixinAdmin.fields + ("repr_expression", )


@admin.register(DatumGroup)
class DatumGroupAdmin(EntityMixinAdmin):
    inlines = [DatumTypeInline, ]